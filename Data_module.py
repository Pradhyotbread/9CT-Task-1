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

def update_data_entry():
    print("|-=-=-=-=-=-= Update Data Entry =-=-=-=-=-=-=|")
    print("Available columns: Driver, Nationality, Race_Wins, Points, Decade")
    driver_name = input("Enter driver name to update: ").strip()
    
    if driver_name not in F1db['Driver'].values:
        print(f"|   - Driver '{driver_name}' not found in dataset       |")
        return
    
    column_name = input("Enter column name to update: ").strip()
    if column_name not in F1db.columns:
        print(f"|   - Column '{column_name}' not found                    |")
        return
    
    new_value = input(f"Enter new value for {column_name}: ").strip()
    
    try:
        F1db.loc[F1db['Driver'] == driver_name, column_name] = new_value
        print(f"|  Updated {driver_name}'s {column_name} to {new_value}|")
    except Exception as e:
        print(f"|   - Error updating data: {str(e)}             |")

    
def UIf1data():
    UI = "null"
    while UI != 'finished':
       print("|-=-=-=-=-=-= F1 Driver's Dataset =-=-=-=-=-=-=|")
       print("|    1 - view Dataset: Applied Data            |")
       print("|    2 - view dataset: Full data               |")
       print("|    3 - View visualisations                   |")
       print("|    4 - Search or filter data                 |")
       print("|    5 - Update a data entry                   |")
       print("|    6 - add/remove data entry                 |")
       print("|    7 - Save changes                          |")
       print("|    0 - Exit                                  |") 
       print("|=-=-=-=-=-=-=-=-=-=-=-=UA=-=-=-=-=-=-=-=-=-=-=|")
       ans = input("|Enter Action according to number: ")
       if ans == '1':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print(driverAge)
            time.sleep(5)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                         |")
       elif ans == '2':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print(F1db)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                         |")
       elif ans == '3':
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
       elif ans == '4':
            time.sleep(2)
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            dataVisual1()
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                         |")
       elif ans == '5':
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            update_data_entry()
            print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=|')
            print("|Returning to start...                         |")
            time.sleep(2)
       elif ans == '6':
               F1db.to_csv('F1Drivers_Dataset.csv', index=False)
               print('|   - Data saved to F1Drivers_Dataset.csv   |')
               time.sleep(2)
       elif ans == '7':
            time.sleep(2)
            #finish later
            print("null")
       elif ans == '0':
            print('|Thank you for checking the database           |')
            print('|=-=-=-=-=-=-=-=-=-=END=-=-=-=-=-=-=--=-=-=-=-=|')
            time.sleep(1)
            UI = "finished"
       else:
            print('|     - input not recognised                   |')
            time.sleep(3)
