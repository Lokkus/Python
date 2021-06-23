#!/usr/bin/env bash


for f in $*; do  # zmienna $* zastepuje wszystkie parametry wejsciowe
  echo "Zmieniam" $f
  chmod 755 $f
done