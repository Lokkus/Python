#!/usr/bin/env bash

function dopasowanie_jeden_znak()
{
  # znak . dopasowywuje jeden znak
  awk '/f.n/' folder/regex.txt

}

function dopasowanie_poczatek_linii()
{
  awk '/^The/' folder/regex.txt
}

function dopasowanie_koniec_linii()
{
  awk '/a$/' folder/regex.txt # plik w ktorym szukamy musi byc sformatowany w odpowiedni sposob czyli LF \n
}

function dopasowanie_zestawu_znakow()
{
  awk '/[FTS]all/' folder/regex.txt

  echo 'dopasowanie oprocz FTS'
  awk '/[^FTS]all/' folder/regex.txt
}

function orowanie()
{
  echo "Chcemy znalesc linie ktore albo zaczynaja sie slowem Numer albo maja ciag cyfr"
  awk '/[Nn]umber|[0-9]{9}/' folder/regex.txt # wyciagamy z pliku wszystkie linie zawierajace slowo Nnumber lub linie zawierajace dokladnie 9 cyfrowe numery

  echo "Lowimy linie zawierajace tylko numery"
  #awk '/[0-9]+/' folder/regex.txt
  awk '{gsub(/[^0-9.]/,"")}1' folder/regex.txt
  awk '{print length($0)}' folder/regex.txt

}

function przesuwanie()
{
  echo "Chcemy wyluskac wszystkie numery z linii w danych pliku"
  awk '{
    for(i=1; i<NF; i++) {
      tmp = match($i, /[0-9]/);
      if (tmp){
        print $i
      }
    }
  }' folder/regex2.txt
}

function zero_or_occurence()
{
  awk '/colou?r/' folder/regex2.txt # tutaj u moze wystepowac zero lub jeden raz
  awk '/cat*/' folder/regex2.txt # tutaj t moze wystepowac zero lub wiecej razy
}


#main
#dopasowanie_jeden_znak
#dopasowanie_poczatek_linii
#dopasowanie_koniec_linii
#dopasowanie_zestawu_znakow
#orowanie
#przesuwanie
zero_or_occurence