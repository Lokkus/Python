#!/usr/bin/env bash

# pobieranie danych wejsiowych znak po znaku

while read ALINE; do
  for ((i=0; i<${#ALINE}; i++)); do #${#ALINE} to jest strlen(napis)
    ACHAR=${ALINE:i:1}
    echo $ACHAR
  done
done