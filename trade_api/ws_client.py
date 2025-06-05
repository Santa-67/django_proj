# ws_client.py
import asyncio
import websockets
import json
import datetime
from collections import defaultdict, deque
import requests

API_URL = "http://127.0.0.1:8000/api/trades/add-trade/"  # Your Django endpoint

TICKER_HISTORY = defaultdict(lambda: deque(maxlen=60))  # Store last 60 seconds of prices
AVG_HISTORY = defaultdict(list)  # Store last 5 minutes for average

async def process_stock_data():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            msg = await websocket.recv()
            data = json.loads(msg)
            ticker = data["ticker"]
            price = data["price"]
            timestamp = data["timestamp"]

            # Store price history
            TICKER_HISTORY[ticker].append((datetime.datetime.fromisoformat(timestamp.replace("Z", "")), price))
            AVG_HISTORY[ticker].append(price)

            # Check for >2% increase in last minute
            if len(TICKER_HISTORY[ticker]) >= 2:
                old_time, old_price = TICKER_HISTORY[ticker][0]
                percent_change = ((price - old_price) / old_price) * 100
                if percent_change > 2:
                    print(f"ALERT: {ticker} price increased by {percent_change:.2f}% in the last minute!")

            # Every 5 minutes, calculate average and POST to Django
            if len(AVG_HISTORY[ticker]) == 300:  # 5 min * 60 sec
                avg_price = sum(AVG_HISTORY[ticker]) / 300
                avg_price = round(avg_price, 2)  # <-- Add this line
                print(f"5-min average for {ticker}: {avg_price:.2f}")
                response = requests.post(API_URL, json={
                    "ticker": ticker,
                    "price": avg_price,
                    "quantity": 0,
                    "side": "buy",
                    "timestamp": timestamp
                })
                print("POST status:", response.status_code, response.text)
                AVG_HISTORY[ticker].clear()

            await asyncio.sleep(0.1)

asyncio.run(process_stock_data())