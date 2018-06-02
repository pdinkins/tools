from time import sleep
import os
import menu
import sys
from scipts import pyscanner3


login = False
run = True
titlestat = [0]

if login == False:
    titlestat.clear()
    titlestat.append(2)


#### Classes
class Admin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

class DateTime():
    def dt(self):
        import datetime
        return datetime.datetime.now()

#### define the class instances
admin1 = Admin('admin', 'password')
dt1 = DateTime()


def title():
    # running titlebar
    print('=' * 80)
    print('PYTHOS\t\t', dt1.dt())
    print('=' * 80)
    
    # subtitle
    if titlestat[0] == 0:
        print('\n\t\tLOGIN')
        print('=' * 80)
    
    elif titlestat[0] == 1:
        print('\n\t\tLOGIN FAILED')
        print('=' * 80)
    
    elif titlestat[0] == 2:
        print('\n\t\tNODE_ADMIN')
        print('=' * 80)




def clear():
    try:
        os.system('cls')
    
    except:
        
        import platform
        ops = platform.system()
        if ops == 'Darwin':
            os.system('clear')

def refresh_screen():
    clear()
    title()




####### LOGIN SEQUENCE #######
while login:
    title()
    usn = input('username: ')
    if usn != admin1.username:
        titlestat.clear()
        titlestat.append(1)
        refresh_screen()
                
    elif usn == admin1.username:
        titlestat.clear()
        titlestat.append(0)
        refresh_screen()
        pasw = input('password: ')

        if pasw == admin1.password:
            titlestat.clear()
            titlestat.append(2)
            refresh_screen()
            print('You are logging in as ', usn)
            refresh_screen()
            break




def rfsm():
    path = input('path>')
    p = rfs(path)
    print(p)


'''
    for root, dirs, files in os.walk(".", topdown=True):
        for file in files:
            print(os.path.join(root, file))

        for name in dirs:
            print(os.path.join(root, name))

        for dir in dirs:
            dirpath = os.path.join(root, dir)
            dirsize = os.path.getsize(dirpath)
            print(index, '\t\t', dirsize, '\t\t', dirpath)
            index += 1
''' 

def rfs(pathname):
    index = 0
    tsizevar = 0

    print('\n\nINDEX\t\tSIZE\t\tDIRECTORY')
    print('=' * 80)
    for root, dirs, files in os.walk(pathname):
        for file in files:
            pathname = os.path.join(root, file)
            size = os.path.getsize(pathname)
            tsizevar += size
            print(index, '\t\t', size, '\t\t', pathname)
            index += 1

    returndata = {'indexed files': index,'totalsize': tsizevar}
    print(returndata)
    input('>')
    return returndata


def rootfile_list():
    spath = 'C:/'
    #spath = '.'
    rootfilelist = os.listdir(spath)
    root_dict = rootfilelist
    try:
        for i in range(0, len(root_dict)):
                path = 'C:/' + root_dict[i]
                subroot = os.listdir(path)
                print('\t', path)
                
                for j in range(0, len(subroot)):
                    print('\t\t',j, subroot[j])

    except (TypeError, NotADirectoryError):
        #print('type error')
        pass
    input('rootfile_list>\t')
    return rootfilelist


def rootfile_list_2():
    spath = 'C:/'
    rootfilelist = os.listdir(spath)
    root_dict = rootfilelist
    
    for i in range(0, len(rootfilelist)):
        print(i, spath + rootfilelist[i])

    input('rootfile_list>\t')
    return rootfilelist




##### PORTAL
'''


'''

## import 
from db import db_interact

#### Menu functions
## Main Menus
def db_main_menu():
    refresh_screen()
    menu.initialize_menu(db_mm, "DB Main Menu")

def db_c_main_menu():
    refresh_screen()
    menu.initialize_menu(db_cm, "DB_contacts Main Menu")

def db_e_main_menu():
    refresh_screen()
    menu.initialize_menu(db_em, "DB_events Main Menu")

def dbmmfunc():
    refresh_screen()
    menu.initialize_menu(db_mm, 'DATABASE MAIN MENU')

def n_menu():
    refresh_screen()
    menu.initialize_menu(n_m, 'NETWORKING MAIN MENU')

def rootinfo():
    refresh_screen()
    menu.initialize_menu(rim, "ROOT_INFO")

def script5run():
    refresh_screen()
    menu.initialize_menu(sc_dct, "Scripts")

### sub defs
def add_contact():
    db_interact.contacts_csv_write()

def add_event():
    db_interact.events_csv_write()

def stable_db():
    os.system("start py stable/DB/dbmain.py")

def tpls_server_start():
    refresh_screen()
    os.system("start py scipts/night_hawk/pynetwork/tpls_server.py")

def tpls_client():
    refresh_screen()
    os.system("start py scipts/night_hawk/pynetwork/testclient.py")

def tpls_serverclient():
    refresh_screen()
    os.system("start py scipts/night_hawk/pynetwork/serverclient.py")

def tpls_serverclient2():
    refresh_screen()
    os.system("start py scipts/night_hawk/pynetwork/node_0_ping.py")

def phy():
    refresh_screen()
    os.system("start py scipts/night_hawk/pynetwork/DB/Physics/physics.py")

#### Menu dictionarys ####
## DATABASE MAIN MENU
db_mm = {
    'Contacts': db_c_main_menu,
    'Events': db_e_main_menu,
    'Physics': phy,
    'quit': menu.quit_menu}

## DATABASE CONTACTS
db_cm = {
    'add': add_contact, 
    'back': db_main_menu
}

## DATABASE EVENTS
db_em = {
    'add': add_event,
    'back': db_main_menu
}

## NETWORK
n_m = {
    'Pyscan' : pyscanner3.pyscan
} 

## SCRIPTS
sc_dct = {
    'back': db_main_menu,
    'tpls': tpls_server_start,
    'tpls_client': tpls_client,
    "tpls_serverclient": tpls_serverclient,
    'node_0': tpls_serverclient2
}

## ROOT INFO
rim = {
    'back': db_main_menu,
    'Root-File-List': rootfile_list_2,
    'rootrat': rootfile_list,
    'stable_db': stable_db,
    'Index-path': rfsm
}

## MAIN MENU
mm = {
    'Scripts': script5run,
    'NETWORKING' : n_menu,
    'DATABASE' : dbmmfunc,
    'ROOT_INFO': rootinfo,
    'QUIT': menu.quit_menu
}

######## APP INTERFACE ########
while run:
    refresh_screen()
    #menu.display_menu(mm, 'root-commands')
    menu.initialize_menu(mm, 'ROOT FILE SYSTEM MAIN MENU')




