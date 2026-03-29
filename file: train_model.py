import yfinance as yf
import pandas as pd

# Download Bitcoin data
data = yf.download("BTC-USD", start="2020-01-01")

# Save dataset
data.to_csv("bitcoin.csv")

print("Data downloaded")
