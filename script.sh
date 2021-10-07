#!/bin/bash

backgroundpath=`gsettings get org.gnome.desktop.background picture-uri`


base_path=${0::-9}
add_path="${base_path}add_to_list.py"
remove_path="${base_path}remove_from_list.py"
cat_path="${base_path}todo.txt"
change_path="${base_path}change_bg.py"


if [ "$1" = "-a" ]
then
    $add_path "$2" "$backgroundpath" "$0"
elif [ "$1" = '-r' ]
then
    $remove_path "$2" "$0"
elif [ "$1" = '-l' ]
then
    cat "${cat_path}"
elif [ "$1" = '--help' ]
then
    printf "\n\n## TodoList implementation in desktop background ##\n\n\nUse :\n    to add something to the list :\n    -a message\n\n    to remove the i-th item of the list\n    -r i\n\n    to list the items in the terminal\n    -l\n\n"
fi

$change_path "$backgroundpath" "$0"

gsettings set org.gnome.desktop.background picture-uri $backgroundpath
