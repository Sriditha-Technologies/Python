import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white",color_codes=True)
a=sns.load_dataset("tips")
sns.boxplot(x='day',y='total_bill',data=a)