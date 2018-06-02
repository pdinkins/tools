import csv
from dbcontacts import *
from events import *
import os


# MENU
# displays a menu, user choice, choice function execution.


'''
USE:
    1. import menu
    2. define menu choice functions
    3. define menu dictionary
        {'menu choice label': corresponding function}
    4. menu.initialize_menu(**menu_dictionary, **menutitle)
'''

def initialize_menu(menu_dictionary, menutitle):
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
            menuchoice = int(input('\nMenu Choice:  '))
        except EOFError:
            return
        menuchoice -= 1
        print()
        menu_dictionary[menulist[menuchoice]]()
    except (IndexError, ValueError):
        print('***invalid choice***')

def clear():
    try:
        os.system('cls')
    
    except:
        
        import platform
        ops = platform.system()
        if ops == 'Darwin':
            os.system('clear')

def quit_menu():
    quit()

def planner_menu():
    initialize_menu(planner_dict, 'DB Main Menu')

def events_menu():
    eventcsvread()
    initialize_menu(events_command_dict, "DB_events")

def contacts_menu():
    initialize_menu(command_dict, "DB_contacts")


planner_dict = {
    'events': events_menu,
    'contacts': contacts_menu
}


while True:
    clear()
    planner_menu()
