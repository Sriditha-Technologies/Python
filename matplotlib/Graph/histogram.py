import matplotlib.pyplot as plt
Population_ages=[22,55,62,45,21,22,34,42,42,44,99,102,110,120,121,122,130,111,115,111,80,75,65,54,44,43,42,48]
bins=[0,10,20,30,40,0,60,70,80,90,100,110,120,130]
plt.hist(Population_ages,bins,histype='bar',rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('histogram')
plt.legend()
plt.show()