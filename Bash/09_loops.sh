#!/usr/bin/env bash

#for loop
for i in `seq 1 10`; do
  echo $i
done
cd ..
for f in `ls`; do
  echo $f
done
cd Bash

count=6
while [ $count -gt 0 ]; do
  echo 'Bilet na 5 koncertow kosztuje dla' $USER: $count\$ 'oraz dodatkowy tekst'
  ((count--))
done

count=0
until [ $count -gt 5 ]; do
  printf "Value of count: %d\n" $count
  let count=count+1
done
