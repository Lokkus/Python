#!/usr/bin/env bash

dir=`pwd`/Album

[ ! -d $dir ] && { echo $dir doesn\'t exist; exit 1; }

cd $dir

new_number_name=''

#zmienna przechowujaca dopasowane elementy: BASH_REMATCH
for f in *.mp3; do
    # shellcheck disable=SC1009
    if [[ "$f" =~ ([[:alpha:]]*)\ -\ ([[:alpha:][:blank:]]*)\ -\ ([[:digit:]]*)\ -\ (.*)$ ]]; then
      echo ${BASH_REMATCH[4]};
      new_str="${BASH_REMATCH[3]}_-_${BASH_REMATCH[4]// /_}" # w ten sposob mozna wygenerowac nowy string w formacie 01_-_Tytul_utworu.mp3
      echo $new_str
    fi
done

