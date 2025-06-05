from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trade
from .serializers import TradeSerializer
from .tasks import notify_price_threshold


class AddTradeView(APIView):
    def post(self, request):
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            trade = serializer.save()
            # Trigger the background task
            notify_price_threshold.delay(trade.ticker, trade.price)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchTradesView(APIView):
    def get(self, request):
        ticker = request.query_params.get("ticker")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        trades = Trade.objects.all()
        if ticker:
            trades = trades.filter(ticker=ticker)
        if start_date and end_date:
            trades = trades.filter(timestamp__range=[start_date, end_date])

        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)
