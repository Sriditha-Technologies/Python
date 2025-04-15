import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK']
}

df = pd.DataFrame(data)

# View the DataFrame
print(df)

# Selecting a column
print(df['Name'])

# Filtering rows
print(df[df['Age'] > 28])

# Adding a new column
df['Salary'] = [50000, 60000, 70000]
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print("Average Age:", average_age)