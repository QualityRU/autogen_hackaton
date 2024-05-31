# filename: bitcoin_price.py

import requests
from datetime import datetime, timedelta

# Get the current price of Bitcoin
response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
current_price = response.json()['bitcoin']['usd']

# Get the date 7 days ago
date_7_days_ago = (datetime.now() - timedelta(days=7)).strftime('%d-%m-%Y')

# Get the price of Bitcoin 7 days ago
response = requests.get(f'https://api.coingecko.com/api/v3/coins/bitcoin/history?date={date_7_days_ago}')
price_7_days_ago = response.json()['market_data']['current_price']['usd']

# Calculate the change in price
price_change = current_price - price_7_days_ago

print(f'Current price: {current_price}')
print(f'Price 7 days ago: {price_7_days_ago}')
print(f'Price change: {price_change}')