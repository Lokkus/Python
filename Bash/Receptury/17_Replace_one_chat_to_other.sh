#!/usr/bin/env bash

# zamieniamy znak podany jako parametr $1 znakiem podanym jako parametr $2 w pliku ktorego nazwa zawarta jest w parametrze $3 a wynik
# to plik ktorego nazwa podana jest przez parametr $4

tr "$1" "$2" <"$3">"$4"