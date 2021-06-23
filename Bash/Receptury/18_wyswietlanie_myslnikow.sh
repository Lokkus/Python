#!/usr/bin/env bash
#dash - wyswietlanie wiersza znakow myslnika
#opcje:   # liczba znakow (domyslnie 72)
#         -c X znak X zastepuje znakl myslnika

function usagexit()
{
  printf "uzycie: %s [-c X] [#]\n" $(basename $0)
  exit 2
} >&2

LEN=72
CHAR="-"

while (( $# > 0 )); do
  case $1 in
    [0-9]*) LEN=$1;;
    -c) shift
        CHAR=$1;;
    *)  usagexit;;
  esac
  shift
done

if (( LEN > 4096 )); then
  echo "Zbyt dluga linia" >&2
  exit 3
fi

# przygotowanie ciagu o odpowiedniej dlugosci
DASHES=" "
for ((i=0; i<LEN; i++)); do
  DASHES="${DASHES}${CHAR}"
done

printf "%s\n" "$DASHES"