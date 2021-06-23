#!/usr/bin/env bash

declare -a TAB
TAB=($(ls -l)) # zeby umiescic cos w tablicy trzeba zastosowac taka deklaracje
for ((i=0; i<${#TAB[@]}; i++)); do
  echo ${TAB[i]}
  ((i++))
done


