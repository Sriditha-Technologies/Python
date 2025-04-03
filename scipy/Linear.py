import numpy as np
from scipy import linalg
a=np.array([(1,2),(3,4)])
b=linalg.inv(a)
print(b)