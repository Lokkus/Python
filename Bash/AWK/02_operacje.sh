#!/usr/bin/env bash

function arithmetic_op()
{
  echo "Dodawanie " $1 "do" $2
  awk 'BEGIN {a = '$1'; b = '$2'; print "(a + b) = ", (a + b) }'
  awk 'BEGIN {a = '$1'; b = '$2'; print "(a - b) = ", (a - b) }'
  awk 'BEGIN {a = '$1'; b = '$2'; print "(a * b) = ", (a * b) }'
  awk 'BEGIN {a = '$1'; b = '$2'; print "(a / b) = ", (a / b) }'
  awk 'BEGIN {a = '$1'; b = '$2'; print "(a % b) = ", (a % b) }'
}

function increment_decrement()
{
  echo 'Inkrementacja, dekrementacja'
  awk 'BEGIN { a = 10; b = a++; printf "Inkrementacja: a = %d, b = %d\n", a, b}'
  awk 'BEGIN { a = 10; b = --a; printf "Dekrementacja: a = %d, b = %d\n", a, b}'
}

function przypisanie()
{
  echo 'Przypisanie'
  awk 'BEGIN { name = "Marcin"; print "My name is", name}'
  awk 'BEGIN { cnt = 10; cnt+=10; print "cnt = ", cnt}' # to samo dla -, *, /, **
  awk 'BEGIN { a = 10; b = 10; if (a == b) print "a == b"; else print "a != b"}' # to samo dla <=, >=, <, >, w ifie moze byc || && !

  # ternary operator
  awk 'BEGIN { a = 10; b = 11; (a < b) ? min = a : min = b; print "min = ", min}'

  #laczenie stringow
  awk 'BEGIN { str = "Hello"; str2 = "World"; str3 = str str2; print str3 }' # tutaj znak zpacji laczy 2 stringi

  # tablica
  awk 'BEGIN {
    arr[0] = 10;
    arr[1] = 11;
    arr[2] = 12;
    arr[3] = 13;
    arr[4] = 14;
    for (i in arr ){
      printf "arr[%d] = %d\n", i, arr[i]
    }
  }'

  awk '$0 ~ 9' folder/marks.txt  # szukamy wszystkich linii zawierajacych cyfre 9, dla niepasujacych dajemy !~
}


#main
#arithmetic_op $1 $2
#increment_decrement
przypisanie