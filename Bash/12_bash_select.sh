#!/usr/bin/env bash
PS3='Choose one world:'
#bash select

select word in "Linux" "bash" "scripting" "tutorial"; do
  echo  "The word you have selected is: "$word
  #Break, otherwise endless loop
  break
done

exit 0