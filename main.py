import pandas as pd
import time 
import sys 

NCISdf = pd.read_csv('C:\Users\pvnpk\Documents\GitHub\9CT-Task-1\F1Drivers_Dataset.csv', on_bad_lines="skip")
print(NCISdf)