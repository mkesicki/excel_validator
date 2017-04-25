#!/usr/bin/python -u
# -*- coding: UTF-8 -*-

import yaml
import sys
import os.path
import time
import argparse
import re
from progress.bar import Bar
from openpyxl.reader.excel import load_workbook
from openpyxl.styles import fills, PatternFill
from openpyxl.utils import column_index_from_string, get_column_letter

from validator import *

# import for pyinstaller
from validator import BaseValidator
from validator import ChoiceValidator
from validator import ConditionalValidator
from validator import CountryValidator
from validator import DateTimeValidator
from validator import EmailValidator
from validator import ExcelDateValidator
from validator import LengthValidator
from validator import NotBlankValidator
from validator import RegexValidator
from validator import TypeValidator

def isValid(settings, value, coordinate, errors, value2 = None):
    #validator list
    classmap = {
        'NotBlank': NotBlankValidator.NotBlankValidator,
        'Type': TypeValidator.TypeValidator,
        'Length': LengthValidator.LengthValidator,
        'Regex': RegexValidator.RegexValidator,
        'Email': EmailValidator.EmailValidator,
        'Choice': ChoiceValidator.ChoiceValidator,
        'Date': DateTimeValidator.DateTimeValidator,
        'ExcelDate': ExcelDateValidator.ExcelDateValidator,
        'Country': CountryValidator.CountryValidator,
        'Conditional': ConditionalValidator.ConditionalValidator
    }

    violations = []
    for data in settings:
        for name  in data:
            validator = classmap[name](data[name])

            if name != 'Conditional':
                result = validator.validate(value)
            else:
                result = validator.validate(value, value2)

            if (result == False):
                violations.append(validator.getMessage())

    if len(violations) > 0:
        errors.append((coordinate, violations))

    return True

def setSettings(config):

    settings = {}
    excludes = []

    print "Get validation config " + config
    stream = file(config, 'r')
    config = yaml.load(stream)

    if 'validators' in config and 'columns' in config.get('validators') :
        settings['validators'] = config.get('validators').get('columns')
    else:
        return False

    if 'default' in config.get('validators') :
        settings['defaultValidator'] = config.get('validators').get('default')
    else:
        settings['defaultValidator'] = None

    if 'excludes' in config:
        for column in config.get('excludes'):
            excludes.append(column_index_from_string(column))
        settings['excludes'] = excludes
    else:
        settings['excludes'] = []

    if 'range' in config:
        settings['range'] = config.get('range')[0] + "1:" + config.get('range')[1]
    else:
        settings['range'] = None

    if 'header' in config:
        settings['header'] = config.get('header')
    else:
        settings['header'] = True

    return settings

def markErrors(errors, excelFile, sheetName, tmpDir, printErrors = False):

    progressBar = Bar('Processing', max = len(errors))

    if os.path.getsize(excelFile) > 10485760:
        print "Log broken cells"
        for error in errors:
            progressBar.next()

            if printErrors.lower() == "true":
                print "Broken Excel cell: " + error[0] + " [ "+ ','.join(error[1]) + " ]"
            else:
                print "Broken Excel cell: " + error[0]

        progressBar.finish();
        return

    #open Excel file
    newFile = os.path.join(tmpDir , "errors_" + time.strftime("%Y-%m-%d") + "_" + str(int(time.time())) + "_" + os.path.basename(excelFile))
    fileName,fileExtension = os.path.splitext(excelFile)

    if fileExtension == '.xlsm':
        wb = load_workbook(excelFile, keep_vba=True, data_only=True)
    else:
        wb = load_workbook(excelFile, data_only=True)

    creator = wb.properties.creator
    ws = wb.get_sheet_by_name(sheetName)

    redFill = PatternFill(start_color='FFFF0000',
        end_color = 'FFFF0000',
        fill_type = 'solid')

    for error in errors:
        progressBar.next()

        print "Broken Excel cell: " + error[0]
        cell =  ws.cell(error[0])
        if printErrors:
            cell.value = ','.join(error[1])
        cell.fill = redFill

    progressBar.finish()
    #save error excel file
    wb.properties.creator = creator
    print "[[Save file: " + newFile + "]]"
    wb.save(newFile)

    return newFile

def validate(settings, excelFile, sheetName, tmpDir, printErrors = False):
    print "Validate Excel Sheet " + sheetName

    errors = []
    #open Excel file
    print "Parse Excel file"
    wb = load_workbook(excelFile, keep_vba=True, data_only=True, read_only=True)
    ws = wb.get_sheet_by_name(sheetName)

    progressBar = Bar('Processing', max=ws.max_row)

    if 'range' in settings and settings['range'] != None:
        settings['range'] = settings['range'] + (str)(ws.max_row)

    #iterate excel sheet
    rowCounter = 0
    for row in ws.iter_rows(settings['range']):
        progressBar.next()
        columnCounter = 0
        rowCounter = rowCounter + 1
        #do not parse empty rows
        if isEmpty(row):
            continue
        for cell in row:
            columnCounter = columnCounter + 1
            try:
                value = cell.value
            except ValueError:
                #case when it is not possible to read value at all from any reason
                column = get_column_letter(columnCounter)
                coordinates = "%s%d" % (column, rowCounter)
                errors.append((coordinates, ValueError))

            #find header (first) row
            if settings['header'] != True:
                if value == settings['header']:
                    settings['header'] = True
                break

            #skip excludes column
            if  hasattr(cell, 'column') and cell.column in settings['excludes']:
                continue

            column = get_column_letter(columnCounter)
            coordinates = "%s%d" % (column, rowCounter)

            if column in settings['validators']:
                name = settings['validators'][column][0].keys()[0]
                if name != 'Conditional':
                    isValid(settings['validators'][column], value, coordinates, errors)
                else:
                    fieldB = settings['validators'][column][0]['Conditional']['fieldB']
                    value2 = ws.cell(fieldB + str(rowCounter)).value
                    isValid(settings['validators'][column], value, coordinates, errors, value2)

            elif settings['defaultValidator'] != None:
                isValid(settings['defaultValidator'], value, coordinates, errors)

    progressBar.finish()

    print "Found %d error(s)" % len(errors)
    if (len(errors) > 0):
        return markErrors(errors, excelFile, sheetName, tmpDir, printErrors)

    return True

def isEmpty(row):

    for cell in row:
        if cell.value:
            return False

    return True

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Mark validation errors in Excel sheet.')
    parser.add_argument('config', metavar = 'config', help = 'Path to YAML config file')
    parser.add_argument('file', metavar = 'file', help = 'Path to excel sheet file')
    parser.add_argument('sheetName', metavar = 'sheetName', help = 'Excel Sheet Name')
    parser.add_argument('tmpDir', metavar = 'tmpDir', help = 'Temporary directory path')
    parser.add_argument('--errors', metavar = 'errors', help = 'Print errors messages in cells marked as invalid')
    args = parser.parse_args()

    settings = setSettings(args.config)

    if settings == False:
        sys.exit("Incorrect config file " + args.config)

    results = validate(settings, args.file, args.sheetName, args.tmpDir, args.errors)

    if results != True:
        if results:
            sys.exit("Validation errors store in: [[" + results + "]]")
        else:
            sys.exit("Invalid file is too big to generate annotated Excel file")

    sys.exit(0)
