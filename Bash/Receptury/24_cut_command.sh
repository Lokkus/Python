#!/usr/bin/env bash

#tresc pliku umieszczona w folder/cut_commands.sh
#foo:bar:baz:qux:quux
#one:two:three:four:five:six:seven
#alpha:beta:gamma:delta:epsilon:zeta:eta:teta:iota:kappa:lambda:mu

function wycinanka()
{
  cut -c 4-10 $1    # -c oznacza character 4-10 oznacza ze z kazdego wiersza w pliku zostana wyciete znaki od 4 do 10 wlacznie
  cut -d ':' -f 5-6 $1 # separujemy po : i wycinamy w tym przypadku wszystkie grupy(pola) poza 5 i 6, inne wariany to 5- czyli wycinamy wszystko od 5 do konca linii
}


#main
wycinanka $1