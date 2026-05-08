import pandas as pd
import matplotlib.pyplot as plt
import time 
import sys 

F1df = pd.read_csv("U:\computingTech\9CT-Task-1\F1Drivers_Dataset.csv", on_bad_lines='skip')
print(F1df)