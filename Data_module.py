import pandas as pd
import matplotlib.pyplot as plt
import time
F1db = pd.read_csv('F1Drivers_Dataset.csv', on_bad_lines='skip')
driverAge = F1db.drop(columns=['Nationality', 'Race_Wins'])
#---Functions---------------------------------------------------------------------------------------------------------#

def preview():
    print(driverAge)


def dataVisual1():
    F1db.plot(x='Driver', y='Points', kind='bar')
    plt.title('F1 Drivers and their lifetime points')
    plt.xlabel('Driver')
    plt.ylabel('Points')
    plt.kind = 'bar'
    plt.show()

def dataVisual2():
    nationality_points = F1db.groupby('Nationality')['Points'].sum().sort_values(ascending=False)
    nationality_points.plot(kind='bar')
    plt.title('lifetime points by Nationality')
    plt.xlabel('Nationality')
    plt.ylabel('Points')
    plt.show()

def dataVisual3():
    decade_points = F1db.groupby('Decade')['Points'].sum().sort_index()
    decade_points.plot(kind='bar')
    plt.title('lifetime points by decade')
    plt.xlabel('Decade')
    plt.ylabel('Points')
    plt.show()

def filterData():

    print("filterable columns: Nationality, Decade")
    column_name = input("Enter column name to filter by: ").strip().title()  
    if column_name not in F1db.columns:
          print(f"|   - Column '{column_name}' not found   |")
          return
    else: 
         filter_value = input(f"Enter value to filter {column_name} by: ").strip().title()
         filtered_data = F1db[F1db[column_name] == filter_value]
         print(filtered_data)

def dataUpdate():
    print("|=-=-=-=-=-=-=-=-=-=-=-=UA=-=-=-=-=-=-=-=-=-=-=|")
    print("Available columns: Driver, Nationality, Race_Wins, Points, Decade")
    driver_name = input("Enter driver name to update: ").strip().title()
    
    if driver_name not in F1db['Driver'].values:
        print(f"|   - Driver '{driver_name}' not found    |")
        return
    
    column_name = input("Enter column name to update: ").strip().title()
    if column_name not in F1db.columns:
        print(f"|   - Column '{column_name}' not found    |")
        return
    
    new_value = input(f"Enter new value for {column_name}: ").strip()
    
    try:
        F1db.loc[F1db['Driver'] == driver_name, column_name] = new_value
        print(f"|  Updated {driver_name}'s {column_name} to {new_value} |")
    except Exception as e:
        print(f"|   - Error updating data: {str(e)}         |")

def addEntry():
      print("|=-=-=-=-=-=-=-=-=-=-=-=UA=-=-=-=-=-=-=-=-=-=-=|")
      driver_name = input("Enter driver name: ").strip().title()
      nationality = input("Enter nationality: ").strip().title()
      race_wins = input("Enter race wins: ").strip()
      points = input("Enter points: ").strip()
      decade = input("Enter decade: ").strip().title()
                    
      new_entry = pd.DataFrame({
                        'Driver': [driver_name],
                        'Nationality': [nationality],
                        'Race_Wins': [int(race_wins)],
                        'Points': [int(points)],
                        'Decade': [decade]
                    })
      F1db = pd.concat([F1db, new_entry], ignore_index=True)
      print(f"|   - Driver '{driver_name}' added           |")

def removeEntry():
     print("|=-=-=-=-=-=-=-=-=-=-=-=UA=-=-=-=-=-=-=-=-=-=-=|")
     driver_name = input("Enter driver name to remove: ").strip().title()
     if driver_name in F1db['Driver'].values:
      F1db = F1db[F1db['Driver'] != driver_name]
      print(f"|   - Driver: '{driver_name}' removed        |")
     else:
      print(f"|   - Driver: '{driver_name}' not found      |")

def UIf1data():
    UI = "null"
    while UI != 'finished':
       print("|-=-=-=-=-=-= F1 Driver's Dataset =-=-=-=-=-=-=|")
       print("|    1 - view dataset: Full data               |")
       print("|    2 - View visualisations                   |")
       print("|    3 - Search or filter data                 |")
       print("|    4 - Update a data entry                   |")
       print("|    5 - add/remove data entry                 |")
       print("|    6 - Save changes                          |")
       print("|    0 - Exit                                  |") 
       print("|=-=-=-=-=-=-=-=-=-=-=-=UA=-=-=-=-=-=-=-=-=-=-=|")
       ans = input("|Enter Action according to number: ")

       if ans == '1':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print(F1db)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                         |")
       elif ans == '2':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print('|   1 - data visualisation: Points by driver   |')
            print('|   2 - data visualisation: points by nation   |')
            print('|   3 - data visualisation: points by decade   |')
            print('|=-=-=-=-=-=-=-=-=-=-=-UA=-=-=-=-=-=--=-=-=-=-=|')
            ans2 = input("|Enter Action according to number: ")
            if ans2 == '1':
                    time.sleep(2)
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
                    dataVisual1()
            elif ans2 == '2':
                    time.sleep(2)
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
                    dataVisual2()
            elif ans2 == '3':
                    time.sleep(2)
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
                    dataVisual3()
            else:
                    print('|     - input not recognised                   |')
                    time.sleep(3)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                         |")
       elif ans == '3':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            filterData()
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                         |")
       elif ans == '4':
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            dataUpdate()
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                         |")
            time.sleep(2)
       elif ans == '5':
             print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
             print("|   1 - add data entry                         |")
             print("|   2 - remove data entry                      |")
             print('|=-=-=-=-=-=-=-=-=-=-=-=UA=-=-=-=-=-=-=-=-=-=-=|')
             time.sleep(2)
             ans3 = input("|Enter Action according to number: ") 
             if ans3 == '1':
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
                    addEntry()
                    time.sleep(2)
                       
             elif ans3 == '2':
                    print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
                    removeEntry() 
                    time.sleep(2)
             else:
                         print('|     - input not recognised                   |')
                         time.sleep(3)
             print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
             print("|Returning to start...                         |")
       elif ans == '6':
            time.sleep(2)
            F1db.to_csv('F1Drivers_Dataset.csv', index=False)
            print('|   - Data saved to F1Drivers_Dataset.csv      |')
            print("null")
       elif ans == '0':
            print('|Thank you for checking the database           |')
            print('|=-=-=-=-=-=-=-=-=-=END=-=-=-=-=-=-=--=-=-=-=-=|')
            time.sleep(1)
            UI = "finished"
       else:
            print('|     - input not recognised                   |')
            time.sleep(3)
