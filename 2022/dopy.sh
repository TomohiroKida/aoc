#!/bin/bash

day=$1
opt=$2
num=$3
if [ $# = 0 ]; then
  echo $0 [0-25] [t]
fi
test=
if [ "${opt}" = t ]; then
  test=_test
fi
src=src/day${day}.py
data=data/day${day}_input${test}${num}.txt
python3 ${src} ${data}
