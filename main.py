import pandas as pd
import time 
import sys 

NCISdf = pd.read_csv('U:\computingTech\9CT-Task-1\ViolentCrimeData.csv', on_bad_lines="skip")
print(NCISdf)