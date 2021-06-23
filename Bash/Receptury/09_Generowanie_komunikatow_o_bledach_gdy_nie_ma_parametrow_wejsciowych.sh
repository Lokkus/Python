#!/usr/bin/env bash

USAGE="uzycie: moj skrypt katalog plikzrodlowy rodzajkonwersji"
FILEDIR=${1:?"Blad. Podaj katalog wejsciowy"} # tutaj wazna jest skladnia ${1:?
FILESRC=${2:?"Blad. Podaj katalog zrodlowy"}
CVTTYPE=${3:? "Blad. ${USAGE}"}

