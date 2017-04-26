#!/bin/bash

green='\e[0;32m'
yellow='\e[33m'
bold='\e[1m'
endColor='\e[0m'

usage() {
  echo -e "
  ${green}excel_validator compiler v1.1:
  ==================================${endColor}
  $0 option

  ${yellow}Available options:
  -b --build  - build executable
  -c --clean  - delete prepared files without executable
  -r --remove - delete all build files with executable
  -h --help   - show this${endColor}
  "
}

prepare_env() {
  echo -e "${green}[*] PREPARING PYTHON2 VIRTUAL ENVIRONMENT${endColor}"
  if [ ! -d env ] ; then
    virtualenv env
  fi
  source env/bin/activate
  pip install -r requirements.txt
  pip install pyinstaller
  source env/bin/activate
}

clean() {
  echo -e "${green}[*] CLEANING BUILD ENVIRONMENT${endColor}"
  rm -rf env build excel_validator.spec 
}

if [ $# -le 0 ] ; then
  usage
  exit 1
fi

for val in $@ ; do
  if [[ ("$val" == "--help") || "$val" == "-h" ]] ; then
    usage
    exit 0
  fi
  if [[ ("$val" == "--build") || "$val" == "-b" ]] ; then
    prepare_env
      echo -e "${green}[*] BUILDING EXECUTABLE${endColor}"
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
  fi

  if [[ ("$val" == "--clean") || "$val" == "-c" ]] ; then
    clean
  fi

  if [[ ("$val" == "--remove") || "$val" == "-r" ]] ; then
    clean
      echo -e "${green}[*] REMOVING BUILD FILES${endColor}"
    rm -rf dist
  fi
done

echo -e "${green}${bold}[*] DONE${endColor}"
