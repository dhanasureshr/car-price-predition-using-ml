import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading the data set

df = pd.read_csv('Car data.csv')

print(df.sample(10))
