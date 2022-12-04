#!/bin/bash
day=$1
if [ $# = 0 ]; then
  echo $0 [0-25] 
  echo "this is for setup directory of day[0-25]"
  exit
fi
src=src/day${day}.py
tmp=src/template.py
if [ ! -e ${src} ]; then
  echo "create ${src}"
  cp ${tmp} ${src}
fi
data=data/day${day}_input.txt
if [ ! -e ${data} ]; then
  vim ${data}
fi
