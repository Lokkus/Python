#!/bin/bash

let RESULT=$1+$2
echo $1+$2=$RESULT    '-> #let RESULT=$1+$2'
declare -i RESULT2
RESULT2=$1+$2
echo $1+$2=$RESULT2 ' -> # declare -i RESULT2; RESULT2=$1+$2'
echo $1+$2=$(($1+$2)) ' -> # $(($1 + $2))'

function substraction
{
  let res=$1-$2
  echo $res
}

function multiplication
{
  let res=$1*$2
  declare -i res2=($1*$2)*2
  echo $res2
  res2=res2**2 # power of 2
  echo $res2
}

substraction 10 7
multiplication 10 7


