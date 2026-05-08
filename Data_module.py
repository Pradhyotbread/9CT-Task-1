import pandas as pd
import matplotlib.pyplot as plt
F1db = pd.read_csv('U:\computingTech\9CT-Task-1\F1Drivers_Dataset.csv', on_bad_lines='skip')

#---Functions---------------------------------------------------------------------------------------------------------#

def Data_Visualisation():
    DriverOrigin = F1db.drop(columns='')
   
    print(F1db)
Data_Visualisation()