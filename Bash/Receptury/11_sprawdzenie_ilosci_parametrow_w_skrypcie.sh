#!/usr/bin/env bash

[ $# -lt 3 ]  && { echo Niewystarczajaca liczba parametrow; exit 1; } \
              || { echo Jest OK; }

function sprawdzanie_wiecej_niz_jednego_warunku
{
  dir=`pwd`/skrypty
  [ -d $dir ] && { echo "Dir $dir istnieje "; cd $dir; } || { echo $dir nie istnieje; }
  # zapamietaj pliki w tablicy
  declare ARRAY
  i=0

  for f in *.txt; do
    ARRAY[$i]="${f}"
    ((i++))
  done

  for ((i=0; i<${#ARRAY[@]}; i++)); do
    echo ${ARRAY[i]}
  done

  # sprawdzenie czy te pliki istnieja
  [ -f ${ARRAY[0]} -a -f ${ARRAY[1]} -a -f ${ARRAY[2]} ] && echo "Plik istnieje";

  echo sprawdzenie zgodnosci ze wzorcem, sposob pierwszy
  for f in *; do    # sprawdzenie zgodnosci ze wzorcem, sposob pierwszy
    [ ${f: -3} = ".sh" ] && \
    echo $f;
  done

echo sprawdzenie zgodnosci ze wzorcem, sposob drugi
  for f in *; do    # drugi sposob, te podwojne nawiasy sa wazne, w ten sposob mozemy uzyskac porownanie do wzorca
    [[ ${f} == *.sh ]] && \
    echo $f;
  done

echo sprawdzenie zgodnosci ze wzorcem, sposob trzeci
  for f in *; do
    [[ ${f} == *.@(txt|sh) ]] && echo $f;  #w ten sposob mozemy dodac kilka roznych rozszerzen plikow
  done
}

sprawdzanie_wiecej_niz_jednego_warunku