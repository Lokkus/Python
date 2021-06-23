#!/usr/bin/env bash

function zmienna_argc()
{
  awk 'BEGIN {print "Arguments = ", ARGC}' $@
}

function zmienne_argc_argv()
{
#  awk 'BEGIN {
#    for(i=0; i<ARGC-1; ++i)
#    {
#      print "ARGV[%d] = %s\n", i, ARGV[i]
#    }
#  }' $@
  awk 'BEGIN {for (i=1; i<ARGC; i++) {print "ARGV["i"] = "ARGV[i] }}' $@
}

#main
#zmienna_argc $@
zmienne_argc_argv $@