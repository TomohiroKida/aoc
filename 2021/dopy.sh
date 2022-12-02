#!/bin/bash

day=$1
opt=$2
num=$3
if [ $# = 0 ]; then
  echo $0 [day] [t]
fi
test=
if [ "${opt}" = t ]; then
  test=_test
fi
src=src/$1.py
data=data/$1_input${test}${num}.txt
python3 ${src} ${data}
