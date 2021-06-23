#!/bin/bash
VAR="Ala ma kota" # global variable
function fun
{
  local VAR="Jestem w funkcji fun" # nie moze byc spacji pomiedzy VAR a = musie byc VAR=
  echo $VAR
}
echo $VAR
fun
