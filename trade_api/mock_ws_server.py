# mock_ws_server.py
import asyncio
import websockets
import json
import random
import datetime

TICKERS = ["AAPL", "GOOG", "MSFT", "TSLA"]

async def send_stock_data(websocket):
    prices = {ticker: 100.0 for ticker in TICKERS}
    try:
        while True:
            for ticker in TICKERS:
                # Simulate price change
                change = random.uniform(-1, 1)
                prices[ticker] += change
                data = {
                    "ticker": ticker,
                    "price": round(prices[ticker], 2),
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
                }
                await websocket.send(json.dumps(data))
            await asyncio.sleep(1)  # Send updates every second
    except Exception as e:
        print(f"Error in send_stock_data: {e}")

async def main():
    async with websockets.serve(send_stock_data, "localhost", 8765):
        print("Mock WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())