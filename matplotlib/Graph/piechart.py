import matplotlib.pyplot as plt
slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']
plt.Pie(slices,label='activities',colors='cols',startangle=90,shadow=True,explode=(0,0.1,0,0),autopct='%1.if%%')
plt.title('Pieplot')
plt.show()