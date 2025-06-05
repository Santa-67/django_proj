# filepath: c:\Users\SANTOSH\OneDrive\Desktop\intern_proj\REST_API\trade_api\trades\tasks.py
from celery import shared_task


@shared_task
def notify_price_threshold(ticker, price):
    # Logic for sending notifications
    print(f"Notification: {ticker} crossed the price threshold of {price}")
