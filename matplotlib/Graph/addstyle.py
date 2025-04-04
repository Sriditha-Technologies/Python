from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x=[5,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[6,15,7]
plt.plot(x,y,'g',label='lineone',linewidth=5)
plt.plot(x2,y2,'c',label='linetwo',linewidth=5)
plt.title('Epic Info')
plt.ylabel('yaxis')
plt.xlabel('xaxis')
plt.legend()
plt.grid(True,color='k')
plt.show()

