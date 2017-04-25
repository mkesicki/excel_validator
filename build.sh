#!/bin/bash
rm -rf env
virtualenv env
source env/bin/activate
pip install -r requirements.txt
pip install pyinstaller
source env/bin/activate

pyinstaller --clean --onefile -p validator \
  --hidden-import=validator.BaseValidator \
  --hidden-import=validator.ChoiceValidator \
  --hidden-import=validator.ConditionalValidator \
  --hidden-import=validator.CountryValidator \
  --hidden-import=validator.DateTimeValidator \
  --hidden-import=validator.EmailValidator \
  --hidden-import=validator.ExcelDateValidator \
  --hidden-import=validator.LengthValidator \
  --hidden-import=validator.NotBlankValidator \
  --hidden-import=validator.RegexValidator \
  --hidden-import=validator.TypeValidator \
  excel_validator.py
rm -rf build excel_validator.spec
