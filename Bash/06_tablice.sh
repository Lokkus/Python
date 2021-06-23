#!/usr/bin/env bash
#deklaracja tablicy 4 elementowej
ARRAY=('el pierwszy' 'el drugi' 'el trzeci' 'el czwarty')

# sizeof tej tablicy
ELEMENTS=${#ARRAY[@]}
for (( i=0; i<ELEMENTS; i++)); do
  echo ${ARRAY[i]}
done
