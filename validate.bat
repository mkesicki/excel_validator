echo %1
python excel_validator.py  "example/example.yml" %1 "Example" %TMP% --errors=true
pause

