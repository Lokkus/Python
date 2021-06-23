#!/usr/bin/env bash

function czytaj()
{
  while read LINE; do
    echo $LINE
  done < $1
}

function czytaj_2()  # dodaje dodatkowe ~~ do wyswietlenia
{
  while read; do echo ~~"$REPLY"~~; done < $1
}

function czytaj_3()
{
  while read REPLY; do echo ~~"$REPLY"~~; done < $1
}



# 'main'
#czytaj $1
#czytaj_2 $1
czytaj_3 $1

