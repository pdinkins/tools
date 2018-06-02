#db_interact.py
'''
This script is used to facilitate to reading and writing of data 
to and from the database files
'''

import csv

#### CONTACTS ####
filestr = 'db/contacts.csv'
# dynamic storage lists
names = []
email = []
phone = []

def dyn_dump_c():
    names.clear()
    email.clear()
    phone.clear()

# read data from db file to dynamic storage lists
def contacts_csv_read():
    dyn_dump_c()
    try:
        with open(filestr) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                names.append(row[0])
                email.append(row[1])
                phone.append(row[2])
    except FileNotFoundError:
        print('Could not find contacts file.\nA new was file created.\n')
        open(filestr, 'w')
        contacts_csv_read()

# user input function 
def contacts_csv_write():
    with open(filestr, 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        name = input('name: ')
        email = input('email: ')
        phone = input('phone: ')
        filewriter.writerow([name, email, phone])

# non-user input function 
def contacts_csv_write_raw(name, email, phone):
    with open(filestr, 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow([name, email, phone])


#### EVENTS #####
filestr2 = 'db/events.csv'
# dyanamic data storage
events = []
dates = []
starttime = []
endtime = []

def dyn_dump_e():
    events.clear()
    dates.clear()
    starttime.clear()
    endtime.clear()

# read data from db file into dynamic storage lists
def events_csv_read():
    dyn_dump_e()
    try:
        with open(filestr2) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                events.append(row[0])
                dates.append(row[1])
                starttime.append(row[2])
                endtime.append(row[3])
    except FileNotFoundError:
        open(filestr2, 'w')
        events_csv_read()
            
# user input function 
def events_csv_write():
    with open(filestr2, 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        event_name = input('Event name: ')
        event_date = input('Event date: ')
        start_time = input('Start time: ')
        end_time = input('Endtime: ')
        filewriter.writerow([event_name, event_date, start_time, end_time])

# non-user input function 
def events_csv_write_raw(event_name, event_date, start_time, end_time):
    with open(filestr2, 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow([event_name, event_date, start_time, end_time])