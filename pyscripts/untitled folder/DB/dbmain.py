import csv
from dbcontacts import *
from events import *


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


def quit_menu():
    quit()




def planner_menu():
    
    while True:
        print('''
        Events : e
        Contacts : c
        Quit : quit
        ''')
        try:
            print('\nEnter command')
            command = input('>  ')
            if command == 'quit':
                print('bye')
                break
            else:
                planner_dict[command]()
        except KeyError:
            print("\n****Invalid Command****\n")



def events_menu():
    while True:
        print('Event Manager\n')
        eventcsvread()
        events_command_menu()
        break
    while True:
        try:
            command = input('\nCommand: ')
            if command == 'exit':
                print('Returning to planner menu')
                break
            else:
                events_command_dict[command]()
        except KeyError:
            print("\n****Invalid Command****\n")


def contacts_menu():
        
    while True:
        print('Contact Manager\n')
        csvread()
        contacts_command_menu()
        
        try:
            command = input('\nCommand: ')
            if command == 'exit':
                print('Returning ot planner menu\n')
                break
            else:
                command_dict[command]()
        except KeyError:
            print("\n****Invalid Command****\n")


planner_dict = {
    'e': events_menu,
    'c': contacts_menu
}

planner_menu()