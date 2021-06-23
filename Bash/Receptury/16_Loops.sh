#!/usr/bin/env bash

function while_loop()
{
  count = 0
  while (( count < $1 )); do
    echo -n $count' '
    (( count++ ))
  done
  echo
}
 while_loop 12

while read -r LINE; do  # wypluje kazda linie oprocz tych ktore zaczynaja sie od a
  [[ ! "$LINE" =~ ^a ]] && echo $LINE
done < $1


function for_loop()
{
  for i in `seq 1.0 .03 2`; do
    echo -n $i' '
  done
}
for_loop

echo

X=$(ls -l)
echo $X
