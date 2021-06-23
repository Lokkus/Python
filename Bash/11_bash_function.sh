#!/usr/bin/env bash
#bash function can be declared in any order

function fun_b
{
  echo Fun B
}

function fun_A
{
  echo $1
}

function fun_D
{
  echo fun_D
}

function fun_C
{
  echo $1
}
#main
#pass parameter for fun_A
fun_A 'Function A'

fun_b

#pass paramterf to fun_C
fun_C 'Function C'
fun_D

