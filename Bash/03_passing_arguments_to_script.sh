#!/usr/bin/env bash

echo $1 $2 $3 # wywolanie ./03_passing_arguments_to_script.sh test test1 test2 wypluje komunikat: test test1 test2

# mozna tez wykorzystac skladnie $@

args=$@
echo ${args[0]} ${args[1]} ${args[2]}
echo "$@"
echo "Number of args passed to script: $#"