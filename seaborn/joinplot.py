import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
x=pd.DataFrame({'Day':[1,2,3,4,5,6,7],'Grocery':[30,80,45,23,51,4,76],'cloths':[13,40,34,23,54,67,98],'utensils':[12,32,27,34,55,67]})
y=pd.DataFrame({'Day':[1,2,3,4,5,6,7],'Grocery':[30,80,45,23,51,4,76],'cloths':[13,40,34,23,54,67,98],'utensils':[12,32,27,34,55,67]})
dta=np.random_multivariate_normal(200)
with sns.axes_style('white'):
    sns.jointplot(x=x,y=y,kind='kde',color='b');