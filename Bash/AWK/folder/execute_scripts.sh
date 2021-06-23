#!/usr/bin/env bash

# mamy plik i wyswietlamy jego zawartosc opisujac kolumny
# plik jest przekazany jako paramter
# $1
function zawartosc_opis_kolumn()
{
    awk 'BEGIN {printf "Sr No\tName\tSub\tMarks\n"} {print}' $1
}

function pokaz_kolumne()
{
  awk '{print $3 "\t" $4}' $1
}

function drukuj_linie_pasujace()
{
  #awk '/r|R/ {print $0}' $1
  awk '/r|R/ {print $3 "\t" $4}' $1  #kiedy chcez znalesc r lub R w okreslonych kolumnach
}

function licz_i_drukuj_pasujace_linie()
{
  awk '/r|R/{cnt++; print $0} END {print "Count = ", cnt}' $1
}

function wyswietl_wiersze_wieksze_niz()
{
  awk 'length($0) > 18' $1
}


#'main'
#zawartosc_opis_kolumn $1
#pokaz_kolumne $1
#drukuj_linie_pasujace $1
#licz_i_drukuj_pasujace_linie $1
wyswietl_wiersze_wieksze_niz $1
