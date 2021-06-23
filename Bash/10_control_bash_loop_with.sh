#!/usr/bin/env bash
cd folder/

DIR=`pwd`

find $DIR -type f | while read file; do
# using POSIX class [:space:] to find space in filenames
if [[ "$file" = *[[:space:]]* ]]; then
#substitute space with "_" character and consequently rename the file
  mv "$file" `echo $file | tr ' ' '_'`
fi;
done