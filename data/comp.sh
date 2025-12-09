#!/bin/bash

year=$1
email=`git config --global user.email`
echo $email

if [[ -d $year ]] && [[ ! -f $year.tar.xz ]]; then
  tar Jcf $year.tar.xz $year
fi

if [[ -f $year.tar.xz ]] && [[ ! -f $year.tar.xz.asc ]]; then
  rm -rf $year
  gpg -r $email -ea $year.tar.xz
fi

if [[ -f $year.tar.xz.asc ]]; then
  rm -f $year.tar.xz
fi
