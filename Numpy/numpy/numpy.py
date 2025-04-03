import numpy as np
import time
import sys
s=range(1000)
print(sys.getsizeof(5)*len(s))
D=np.arange(1000)
print(D.size*D.itemsize)