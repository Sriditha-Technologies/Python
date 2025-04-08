import matplotlib.pyplot as plt

players = ['Messi', 'Ronaldo', 'Neymar', 'Mbappe']
ratings = [93, 92, 91, 90]

plt.bar(players, ratings, color='blue')
plt.xlabel('Players')
plt.ylabel('Ratings')
plt.title('FIFA Player Ratings')
plt.show()