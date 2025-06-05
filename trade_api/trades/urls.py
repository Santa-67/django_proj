# filepath: c:\Users\SANTOSH\OneDrive\Desktop\intern_proj\REST_API\trade_api\trades\urls.py
from django.urls import path
from .views import AddTradeView, FetchTradesView

urlpatterns = [
    path("add-trade/", AddTradeView.as_view(), name="add-trade"),
    path("fetch-trades/", FetchTradesView.as_view(), name="fetch-trades"),
]
