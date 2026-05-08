import pandas as pd
import matplotlib.pyplot as plt


#---Functions---------------------------------------------------------------------------------------------------------#

def Data_Visualisation():
    F1db = pd.read_csv('U:\computingTech\9CT-Task-1\F1Drivers_Dataset(in) (1).csv', on_bad_lines='skip')
    print(F1db)