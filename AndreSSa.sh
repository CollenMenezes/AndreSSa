#!/bin/bash 
#Author:
#Give credits if u use any parte of this code.

#Colors
R="\e[91m"
RT="\e[0m"
P="\e[95m"
BD="\e[1m"

logo() {

printf "    _                  _                 ${P}____    ____${RT}          \n"
printf "   / \     _ __     __| |  _ __    ___  ${P}/ ___|  / ___|${RT}    __ _ \n"
printf "  / _ \   | \'_ \   / _\` | | \'__|  / _ \ ${P}\___ \  \__  \ ${RT}  / _\` |\n"
printf " / ___ \  | | | | | (_| | | |    |  __/  ${P}___) |  ___) |${RT} | (_| |\n"
printf "/_/   \_\ |_| |_|  \__,_| |_|     \___| ${P}|____/  |____/${RT}   \__,_|\n"
printf "\n"

}

#function create another file
create_another_file() {
logo
printf "[-] DO YOU WANT TO CREATE ANOTHER FILE? (Y/N) "
read create_file

if [[ $create_file = Y || $create_file = y ]]; then
   bash AndreSSa.sh
elif [[ $create_file = N || $create_file = n ]]; then
    clear
    logo
    printf "${BD}${R}[-] SEE YOU!${RT}"
    sleep 3
    clear
    exit 0
else
    clear
    logo
    printf "[-] THIS OPTION IS NOT VALID!"
    create_another_file
fi

}

#function folder creation
func_folder() {
clear
logo

printf "[-] WELCOME TO THE ${BD}BASH TEXT CONVERTER!${RT}"
sleep 2
clear

logo

sleep 1
printf "[-] CREATE A FOLDER NAME: "
read var_folder

if [ -z $var_folder ]; then
    clear
    logo
    printf "${R}${BD}[-] THE FOLDER NAME CANNOT BE EMPTY!${RT}"
    sleep 5
    bash AndreSSa.sh
fi

clear
logo
sleep 1

if [[ -e Files/$var_folder.txt ]]; then
    rm -rf Files/$var_folder.txt
    printf "${R}${BD}[-] THIS FILE ALREADY EXIST AND HAS BEEN DELETED!${RT}"
    sleep 5
    bash AndreSSa.sh
else
    touch Files/$var_folder.txt
fi

}

#function text converter
func_text() {
clear
logo

sleep 1
read -p "[-] PAST OR INSERT YOUR TEXT HERE: " var_text
clear
logo

if [ -z $var_text ]; then
    clear
    logo
    printf "${R}${BD}[-] THE TEXT FIELD CANNOT BE EMPTY!${RT}"
    sleep 5
    bash AndreSSa.sh
fi

printf "[-] ${BD}CONVERTING...${RT}"
sleep 3
clear
logo

printf "[-] DONE!"
sleep 1


touch Files/$var_folder.txt
echo $var_text | tr [:lower:] [:upper:] > Files/$var_folder.txt
sleep 2

clear
logo

printf "[-] A NEW TEXT FILE HAS BEEN CREATED!"
sleep 3
clear

create_another_file

}

if [ -d "Files" ]; then
    func_folder
    func_text
else
    mkdir Files
    func_folder
    func_text
fi
