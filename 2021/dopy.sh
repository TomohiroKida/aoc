#!/bin/bash

day=$1
opt=$2
if [ $# = 0 ]; then
  echo $0 [day] [t]
fi
test=
if [ "$opt" = t ]; then
  test=_test
fi
src=src/$1.py
data=data/$1_input$test.txt
python3 $src $data
