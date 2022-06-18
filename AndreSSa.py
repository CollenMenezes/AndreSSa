#AndreSSa Python version.
#Author: CollenMenezes

import os
import time

def main():

    class colors:
        red = "\u001b[31m"
        reset = "\u001b[0m"
        magenta = "\u001b[35m"
        bold = "\u001b[1m"


    def banner():
        os.system("clear")
        print (f"     _                  _                 {colors.magenta}{colors.bold}____    ____{colors.reset}          ")
        print (f"    / \     _ __     __| |  _ __    ___  {colors.magenta}{colors.bold}/ ___|  / ___|{colors.reset}    __ _ ")
        print (f"   / _ \   | '_ \   / _` | | '__|  / _ \ {colors.magenta}{colors.bold}\___ \  \___ \{colors.reset}   / _` |")
        print (f"  / ___ \  | | | | | (_| | | |    |  __/  {colors.magenta}{colors.bold}___) |  ___) |{colors.reset} | (_| |")
        print (f" /_/   \_\ |_| |_|  \__,_| |_|     \___| {colors.magenta}{colors.bold}|____/  |____/{colors.reset}   \__,_|")

    banner()
    print (f"\n[-] WELCOME TO THE {colors.bold}PYTHON TEXT CONVERTER!{colors.reset}")
    time.sleep(3)

    #create folder txt
    def create_folder():
        banner()
        time.sleep(1)
        global create_file_name
        create_file_name = input("\n[-] CREATE A FOLDER NAME: ")

    create_folder()

    while create_file_name == "":
        banner()
        print (f"\n[-] {colors.red}{colors.bold}THE FOLDER FIELD CANNOT BE EMPTY!{colors.reset}")
        time.sleep(4)
        create_folder()

    if os.path.exists ("Files/" + create_file_name + ".txt"):
        file = open("Files/" + create_file_name + ".txt", "at")
    else:
        file = open("Files/" + create_file_name + ".txt", "x")

    file.close()

    #enter text
    def enter_text():
        banner()
        time.sleep(1)
        global var_text
        var_text = input("\n[-] PASTE OR ENTER THE TEXT HERE: ")
        time.sleep(2)

    enter_text()

    while var_text == "":
        banner()
        print (f"[-] THE TEXT FIELD CANNOT BE EMPTY!")
        time.sleep(4)
        enter_text()

    banner()
    print (f"\n[-] {colors.bold}CONVERTING...{colors.reset}")
    time.sleep(3)

    file = open ("Files/" + create_file_name + ".txt", "a")
    file.write("\n" + var_text.upper())
    file.close()

    banner()
    print (f"\n[-] DONE! A NEW TEXT FILE HAS BEEN CREATED!")
    time.sleep(3)



    def func_option():

        banner()
        global again
        again = input("\n[-] DO YOU WANT TO MAKE A NEW CONVERTING? (Y/N) ")

        if again == "y" or again == "Y":
            main()
        elif again == "n" or again == "N":
            banner()
            print ("\n[-] SEE YOU!")
            time.sleep(3)
            os.system("clear")
            exit()
        elif again == "":
            banner()
            print (f"\n[-] {colors.red}{colors.bold}INVALID OPTION!{colors.reset}")
            time.sleep(3)
            func_option()
        else:

            banner()
            print (f"\n[-] {colors.red}{colors.bold}INVALID OPTION!{colors.reset}")
            time.sleep(3)
            func_option()

    func_option()

main()
