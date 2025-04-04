import pandas as pd
XYZ_web={'Day':[1,2,3,4,5,6],'visitors':[1000,700,6000,1000,400,350],'bounce_rate':[20,20,23,15,10,34]}
df=pd.DataFrame(XYZ_web)
print(df.head(2))