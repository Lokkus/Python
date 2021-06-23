#!/usr/bin/env bash

aflag=
bflag=

while getopts 'ab:' OPTION; do
  case $OPTION in
    a)  aflag=1;;
    b)  bflag=1;;
    ?)  printf "Uzycie: $s: [ -a][ -b wartosc parametry\n" $(baseneme $0) >&2
        exit 2
        ;;
  esac
done

shift $(($OPTIND - 1))

if [ "$aflag" ]; then
  printf "Opcja -a wprowadzona\n"
fi

if [ "$bflag" ]; then
  printf "Opcja -b $s wprowadzona\n" "$bflag"
fi

printf "Pozostale parametry to: %s\n" "$*"


