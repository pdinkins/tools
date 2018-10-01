menuLogo = '''
    888888  88   88   dP""b8  88  dP    88b 88  88  88""Yb  .dP"Y8
    88__    88   88  dP   `"  88odP     88Yb88  88  88__dP  `Ybo."
    88""    Y8   8P  Yb       88"Yb     88 Y88  88  88""Yb  o.`Y8b
    88      `YbodP'   YboodP  88  Yb    88  Y8  88  88oodP  8bodP'
'''

import random
import platform
import os
import csv

__drivers = []
__drivers_num = []
__driver_list = []

    

class Driver:
    def __init__(self, name, num_driven):
        self.name = str(name)
        self.has_driven = int(num_driven)


class FileObj:
    def __init__(self):
        self._drivers_csv_file = "drivers.csv"


def csv_read(fileobj):
    try:
        with open(fileobj) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                __drivers.append(row[0])
                __drivers_num.append(row[1])
    except FileNotFoundError:
        print("you're fucked")


def generate_driver_objs():
    for i in range(len(__drivers)):
        obj = Driver(__drivers[i], __drivers_num[i])
        __driver_list.append(obj)
        print(obj, __drivers[i], __drivers_num[i], __driver_list[i])


def title_bar():
    print("=" * 80)

def title():
    title_bar()
    print(menuLogo)
    title_bar()

def clear():
    ops = platform.system()
    if ops == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def refresh_screen():
    clear()
    title()


def initialize_menu(menu_dictionary, menutitle):
    refresh_screen()
    menulist = list(menu_dictionary.keys())
    j = 1
    print('\n' + menutitle, '\n')
    for i in range(0,len(menulist)):
        print(j,'-', menulist[i])
        j += 1 
    choose_from_menu(menulist, menu_dictionary)


def choose_from_menu(menulist, menu_dictionary):
    try:
        try:
            menuchoice = int(input('\n>>> '))
            if menuchoice == 0:
                quit()
        except EOFError:
            return
        menuchoice -= 1
        print()
        menu_dictionary[menulist[menuchoice]]()
    except (IndexError, ValueError):
        print('bruh thats not a choice')
    
def fuck_a_nib():
    generate_driver_objs()
    number = random.randint(0, 29)
    print("\n\nCongrats ", __drivers[number], " you get to drive.")
    input("\nPress Enter>>>")


def save():
    pass

fanmenu = {
    "FUCK A NIB": fuck_a_nib
    #"save": save
}


def __main_menu_fuck_a_nib():
    initialize_menu(fanmenu, "Press 1 and Enter to fuck over a Nib")


def main():
    data = FileObj()
    csv_read(data._drivers_csv_file)
    while True:
        __main_menu_fuck_a_nib()

if __name__ == "__main__":
    main()
