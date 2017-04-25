# Excel Validator 

This is simple Python script to validate content in Excel files. It contains most common validators. Of course this
can be extended. Validation rules are stored in *YAML* files.

It was created in my *free* time to improve process of parsing excel files in my company. 
 
## Requirements

Python 2.7
 
All necessary python libraries are listed in [requirements.txt](../master/requirements.txt)
 
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
   --errors errors  Print errors messages in cells marked as invalid
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

Script will create new Excel file with marked errors (red background for invalid cells).
If ```--errors=true``` option is set, script will also print validator message in invalid cells.
Example file with errors *errors_2017-04-25_1493102119_excel.xlsx* is attached to repository in example directory.  
  
## Windows user bonus

[validate.bat](../master/validate.bat) contains example usage (same as in this documentation) of script.
In Windows you can Drag & Drop Excel file on *validate.bat* script and it should execute validation. Of course you 
should change content of this file according to your needs.

## NOTE
This script should not change original Excel file. Of course it is always good to have and work on copy :)

## Changes to script
You can do whatever you want & need with this script. I will be more than happy if it will be useful for you and you will make it script better.