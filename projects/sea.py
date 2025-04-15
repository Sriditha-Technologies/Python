import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a scatter plot with a regression line
sns.lmplot(x='total_bill', y='tip', data=tips)

# Add titles and labels
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')

# Show the plot
plt.show()