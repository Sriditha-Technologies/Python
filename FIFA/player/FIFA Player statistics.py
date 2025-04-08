import pandas as pd

# Sample player data (usually you'd retrieve this from an API or database)
data = {
    'Player': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar', 'Kylian Mbappe'],
    'Rating': [93, 92, 91, 90]
}

df = pd.DataFrame(data)
print(df)

# Calculate the average rating
average_rating = df['Rating'].mean()
print(f"The average player rating is: {average_rating}")