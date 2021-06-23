#!/usr/bin/env bash
#declare
declare -a ARRAY

#Link filedescriptor 10 with stdin
exec 10<&0
#stdin replaced with a file suppleid as a first argument
exec < $1
let count=0

while read LINE; do
  ARRAY[$count]=$LINE
  ((count++))
done

echo "Number elements: " ${#ARRAY[@]}
#echo array's content
echo ${ARRAY[@]}
#restore stdin from filedescriptor 10 and close filedescriptor 10
exec 0<&10 10<&-
