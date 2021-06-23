#!/usr/bin/env bash

ARRAY=(ala ela ula ola)
for ((i=0; i < ${#ARRAY[@]}; i++)); do # #ARRAY[@] to sizeof tablicy
  echo ${ARRAY[i]}
done