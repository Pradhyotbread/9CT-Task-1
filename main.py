import pandas as pd
import time 
import sys 

NCISdf = pd.read_csv('Data/NCIS_Background_Checks.csv', on_bad_lines="skip")
print(NCISdf)