import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("bitcoin.csv")

# Use closing prices
data = data[['Close']]

# Create prediction column
data['Prediction'] = data[['Close']].shift(-10)

# Features
X = np.array(data.drop(['Prediction'], axis=1))[:-10]
y = np.array(data['Prediction'])[:-10]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next prices
prediction = model.predict(X[-10:])

print("Next price predictions:")
print(prediction)

# Plot
plt.plot(data['Close'])
plt.title("Crypto Price Prediction")
plt.show()
