import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
a=sns.load_dataset("Iris")
b=sns.FacetGrid(a,col="species")
b.map(plt.hist,"sepal_length")