#!/usr/bin/env bash

directory_list="Koniec $(for i in /*; do [ -d "$i" ] && echo $i; done)" # Koniec /bin /boot /dev /etc /home /lib /lib64 /media /mnt /opt /proc /root /run /sbin /snap /srv /sys /tmp /usr /var

echo 'Wybierz katalog: ' # komunikat opisujacy liste opcji

until [ "$directory_list" == "Koniec" ]; do
  printf "%b" "\a\n\nLista dostepnych katalogow:\n"
  select directory in $directory_list; do
    if [ "$directory" = "Koniec" ]; then
      echo "Koniec przetwarzania katalogow "
      break
    elif [ -n "$directory" ]; then
      echo "Wybrana opcja: $REPLY, przetwarzanie katakogu $directory ..."
      #instrukcje przetwarzania katalogu
      break
    else
      echo "Bledny wybor! "
    fi
  done
done
