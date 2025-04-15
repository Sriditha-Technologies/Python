import matplotlib.pyplot as plt

#sample data
x=[1,2,3,4]
y=[2,4,6,8]

#create plot
plt.plot(x,y)

#add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")

#display plot
plt.show()