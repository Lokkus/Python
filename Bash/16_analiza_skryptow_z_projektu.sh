run_name=$2
input_list=$1

echo $1
echo $2

sciecha='Bash/'${input_list#"folder/"} # ta konstrukcja pozwala na wyciecie fragmentu sciezki
sciecha2=${input_list/"folder/"/"XXX/"} # jak wyzej
nazwa=$(basename $input_list) # ta konstrukcja pozwala nam na wyciagniecie nazwy pliku z dlugiej sciezki

echo $sciecha
echo $sciecha2
echo $nazwa

# czytanie z pliku

list_list=$(cat folder/list.txt)
for list in $list_list; do
  tmp=${list##*/} # to samo co echo $(basename $list)
  echo ${tmp%.*} # pozbywamy sie " na koncu nazwa % wzorzec - usuniecie najkrótszegop ciagu koncowego zgodnego ze wzrocem

done