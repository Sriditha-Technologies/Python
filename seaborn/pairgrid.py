import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
a=sns.load_dataset("flights")
b=sns.PairGrid(a)
b.map(plt.scatter)