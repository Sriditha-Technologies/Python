import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
a=sns.load_dataset("tips")
sns.relplot(x='time',y='tip',data=a,kind='line')