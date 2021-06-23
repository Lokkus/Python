#!/usr/bin/env bash

# w tym skrypcie zmieniam nazwy plikow przeslanych przez paramter "$@"
# zamieniamy wszystkie pliki zawierajace spacje przekazane przez $@ na pliki z podkreslnikiem
for f in "$@"; do
    mv "${f}" "${f// /_}"
done