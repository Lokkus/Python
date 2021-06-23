#!/usr/bin/env bash
directory=`pwd`

#jeszcze raz
cd ..
directory=`pwd`
array=($(ls -d */))  #zapamietujemy w tablicy wszystkie pliki i katalogi w danym folderze
if [ -d $directory/${array[0]} ]; then
  echo "Directory exists"
  echo $directory/${array[0]}
else
  echo "Directory doesn't exist"
fi