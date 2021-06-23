#!/usr/bin/env bash

function asort_fun()
{
  # sortowanie elementow tablicy
  awk 'BEGIN {
    arr[0] = "One"
    arr[1] = "Two"
    arr[2] = "Three"

    print "Array element before sorting:"

    for (i in arr) {
      print arr[i]
    }
    asort(arr)
    print "Array elements after soring:"

    for(i in arr){
      print arr[i]
    }
  }'
}

function gawk_fun()
{
  # globalna zamiana wyrasow zgodnie ze wzorcem
  # parametr przekazujemy jako $1, gdzie jest to treść skrypt $0 w print okazuje cala tresc
  # celem jest zamiana wszystkich wyrazow zawierajacych slowo kot na KOT oraz slowo zawierajace color na COLOR

  awk '{gsub("kot", "KOT"); gsub("color", "COLOR"); print $0}' $1

  # w tym przypadku zastepujemy wszystkie cyfry znakami xxx
  awk '{gsub("[1-9]", "x"); print $0}' $1
}

function split_fun()
{
  # to jest funkcja ktora dzieli dany string na poszczegolne elementy w oparciu o 3ci parametr
  # celem jest przeszukanie pliku i znalezienie numerkow w tekscie
  awk 'BEGIN{temp = 0}{
    split($0, arr);
    for(i in arr){
      if (temp = match(arr[i], /[0-9]/)){
        temp = 0;
        print arr[i]
      }
    }
  }' $1
}
#main
#asort_fun
#gawk_fun $1
split_fun $1