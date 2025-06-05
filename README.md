REST API DEVELOPMENT

To run the admin:
a) Direct to folder trade_api
b) Run the command: python manage.py runserver
c) Redirect to admin panel

To post trades:
a) http://127.0.0.1:8000/api/trades/add-trade/
b) Example JSON:
      {
  "ticker": "AAPL",
  "price": 150.5,
  "quantity": 10,
  "side": "buy",
  "timestamp": "2025-06-05T12:00:00Z"
}

To fetch trades:
a) http://127.0.0.1:8000/api/trades/fetch-trades/
b) http://127.0.0.1:8000/api/trades/fetch-trades/?ticker=AAPL&start_date=2025-06-01T00:00:00Z&end_date=2025-06-05T23:59:59Z(filter by date and other tickers)

PostgreSql Integration:
a) Open psql command line : psql -U postgres -d trade_db
b) Password: tasveer12
c) Run Commands:
    \dt
    SELECT * FROM trades_trade;
    SELECT * FROM trades_trade WHERE ticker = 'AAPL';

Using Celery and Redis
a) Go to the folder trade_api
b) Run Command: celery -A trade_api worker --loglevel=info --pool=solo
c) Notifications can be seen on the server


REAL TIME DATA PROCESSING

a) Run trade_api/mock_server.py
b) Then run ws_client.py
c) Every 5 minutes an average can be seen

CLOUD INTEGRATION WITH AWS

https://www.loom.com/share/ebd3fdbab45e43178687875e280cc77a?sid=61c99666-cde2-4374-aadb-9a84b0c38ed2


