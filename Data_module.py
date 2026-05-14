import pandas as pd
import matplotlib.pyplot as plt
import time
F1db = pd.read_csv('U:\computingTech\9CT-Task-1\F1Drivers_Dataset.csv', on_bad_lines='skip')
driverDecade = F1db.drop(columns=['Championships', \
    'Race_Entries', \
    'Race_Starts', \
    'Pole_Positions', \
    'Race_Wins', \
    'Podiums', \
    'Points', \
    'Nationality', \
    'Pole_Rate', \
    'Win_Rate', \
    'Podium_Rate', \
    'Years_Active'])
#---Functions---------------------------------------------------------------------------------------------------------#

def driverNational():
    DriverOrigin = F1db.drop(columns=['Championships', \
    'Race_Entries', \
    'Race_Starts', \
    'Pole_Positions', \
    'Race_Wins', \
    'Podiums', \
    'Points', \
    'Decade', \
    'Pole_Rate', \
    'Win_Rate', \
    'Podium_Rate', \
    'Years_Active'])
    print(DriverOrigin)

def DataMain():
    TestedData = F1db.drop(columns=['Championships', \
    'Race_Entries', \
    'Race_Starts', \
    'Pole_Positions', \
    'Race_Wins', \
    'Podiums', \
    'Pole_Rate', 
    'Podium_Rate', \
    'Years_Active'])
    print(TestedData)

def preview():
    driverDecade.xs


def dataVisual1():
    F1db.plot(kind='bar', x='Driver', y='Points')


def UIf1data():
    UI = "null"
    while UI != 'finished':
       print("|-=-=-=-=-=-= F1 Driver's Dataset =-=-=-=-=-=-=|")
       print("|    1 - view Dataset: driver nationality      |")
       print("|    2 - view dataset: Driver decade           |")
       print("|    3 - view dataset: main data               |")
       print("|    4 - view dataset: Full data               |")
       print("|    5 - View visualisation                    |")
       print("|    6 - Search or filter data                 |")
       print("|    7 - Update a data entry                   |")
       print("|    8 - Save changes                          |")
       print("|    9 - Exit                                  |") 
       print("|=-=-=-=-=-=-=-=-=-=-=-=UA=-=-=-=-=-=-=-=-=-=-=|")
       ans = input("|Enter Action according to number: ")
       if ans == '1':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            driverNational()
            time.sleep(5)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                          |")
       elif ans == '2':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            preview()
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returing to start...                          |")
       elif ans == '3':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            DataMain()
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returing to start...                          |")
       elif ans == '4':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            F1db
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returing to start...                          |")
       elif ans == '5':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            dataVisual1() # unfinished value
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returing to start...                          |")
       elif ans == '6':
            time.sleep(2)
            #blank value of current
            print("e")
       elif ans == '7':
            time.sleep(2)
            #finish later
            print("null")
       elif ans == '8':
            time.sleep(2)
            #unfinished
            print("null")
       elif ans == '9':
            print('|Thank you for checking the database           |')
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            time.sleep(1)
            UI = "finished"
       else:
            print('|input not recognised                          |')
            time.sleep(3)


# practice code
UIf1data()

