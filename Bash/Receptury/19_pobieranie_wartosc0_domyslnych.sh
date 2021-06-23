#!/usr/bin/env bash

# parametr domyslny
MY_PATH=${1:-"/home"} # tutaj generujemy defaultowa sciezke, pomiedzy - a / nie moze byc kurwa spacji

if [[ -e $MY_PATH ]]; then
  echo "Istnieje"
  #FZ=$(ls -s $MY_PATH | cut -d ' ' -f 1)
  set -- $(ls -s "$MY_PATH")
fi
echo $FZ



