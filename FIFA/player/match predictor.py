from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Sample data
data = {
    'Home Team Rating': [85, 90, 82, 78, 88],
    'Away Team Rating': [80, 86, 78, 75, 87],
    'Home Win': [1, 1, 1, 0, 1]  # 1 if home team wins, 0 otherwise
}

df = pd.DataFrame(data)

# Features and target
X = df[['Home Team Rating', 'Away Team Rating']]
y = df['Home Win']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)
print(predictions)