import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2],label='exampleone')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label="exampletwo",color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('myplot yo!')
plt.show()