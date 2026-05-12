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