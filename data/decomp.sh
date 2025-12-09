#!/bin/bash

year=$1

if [[ -f $year.tar.xz.asc ]] && [[ ! -f $year.tar.xz ]]; then
  gpg -o $year.tar.xz -d $year.tar.xz.asc
fi

if [[ -f $year.tar.xz ]] && [[ ! -d $year ]]; then
  rm -f $year.tar.xz.asc
  tar xf $year.tar.xz
fi

if [[ -d $year ]]; then
  rm -f $year.tar.xz
fi
