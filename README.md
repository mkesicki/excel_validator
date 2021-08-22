# Excel Validator

Excel Validator is used to validate different constraints of excel column through a Validation rules  stored in *YAML* files.

constraints to be checked :
    -   Base Validator
    -   Choice Validator
    -   Condition Validator
    -   Country Validator
    -   DateTime Validator
    -   Email Validator
    -   Excel Date Validator
    -   Length Validator
    -   NotBlank Validator
    -   Regex Validator
    -   Type Validator
## Requirements

1. Python 3
2. All necessary python libraries are listed in [requirements.txt](../master/requirements.txt)

## Script parameters
 ```commandline
 $ python excel_validator.py  -h
 usage: excel_validator.py [-h] [--errors errors] config file sheetName tmpDir

 Mark validation errors in Excel sheet.

 positional arguments:
   config           Path to YAML config file
   file             Path to excel sheet file
   sheetName        Excel Sheet Name
   tmpDir           Temporary directory path

 optional arguments:
   -h, --help       show this help message and exit
   --errors errors  Print errors messages without generating excel file with errors
```

## Example usage

usage for *example/excel.xlsx* file

```commandline

/PATH/excel_validator>python excel_validator.py "example/example.yml" /PATH/excel.xlsx "Example" "/tmp" --errors=true
Get validation config example/example.yml
Validate Excel Sheet Example
Parse Excel file
Processing |################################| 5/5
Found 22 error(s)
Processing |#                               | 1/22Broken Excel cell: C2
Processing |##                              | 2/22Broken Excel cell: F2
Processing |####                            | 3/22Broken Excel cell: H2
Processing |#####                           | 4/22Broken Excel cell: M2
Processing |#######                         | 5/22Broken Excel cell: A3
Processing |########                        | 6/22Broken Excel cell: D3
Processing |##########                      | 7/22Broken Excel cell: F3
Processing |###########                     | 8/22Broken Excel cell: G3
Processing |#############                   | 9/22Broken Excel cell: H3
Processing |##############                  | 10/22Broken Excel cell: I3
Processing |################                | 11/22Broken Excel cell: K3
Processing |#################               | 12/22Broken Excel cell: M3
Processing |##################              | 13/22Broken Excel cell: A4
Processing |####################            | 14/22Broken Excel cell: E4
Processing |#####################           | 15/22Broken Excel cell: F4
Processing |#######################         | 16/22Broken Excel cell: H4
Processing |########################        | 17/22Broken Excel cell: K4
Processing |##########################      | 18/22Broken Excel cell: M4
Processing |###########################     | 19/22Broken Excel cell: A5
Processing |#############################   | 20/22Broken Excel cell: B5
Processing |##############################  | 21/22Broken Excel cell: J5
Processing |################################| 22/22Broken Excel cell: M5

[[Save file: /tmp/errors_2017-04-25_1493102119_excel.xlsx]]
Validation errors store in: [[/tmp/errors_2017-04-25_1493102119_excel.xlsx]]

/PATH/excel_validator>pause
Press any key to continue . . .
```

## Windows user bonus

[validate.bat](../master/validate.bat) contains example usage (same as in this documentation) of script.
In Windows you can Drag & Drop Excel file on *validate.bat* script and it should execute validation. Of course you
should change content of this file according to your needs.
