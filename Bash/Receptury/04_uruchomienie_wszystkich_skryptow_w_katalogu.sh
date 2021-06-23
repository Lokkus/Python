#!/usr/bin/env bash

dir=`pwd`/skrypty
for s in $dir/*; do [ -f $s -a -x $s ] && $s; done