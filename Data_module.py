import pandas as pd
import matplotlib.pyplot as plt
F1db = pd.read_csv('U:\computingTech\9CT-Task-1\F1Drivers_Dataset.csv', on_bad_lines='skip')

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

def driverYear():
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
    print(driverDecade)
driverYear()

def dataVisual1():
    F1db.plot(kind='bar', x='Driver', y='Points')
dataVisual1()

def UIf1data():
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
    print("|=-=-=-=-=-=-=-=-=-=-=-=AA=-=-=-=-=-=-=-=-=-=-=|")
    UI = "null"
    while UI != 'finished':
        ans = input("Enter Action according to number: ")
        if ans == 1:
            print