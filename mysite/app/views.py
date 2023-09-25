from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StockInfoSerializer
from .models import StockInfo
import yfinance as yf
import pandas as pd

class StockInfoView(APIView):
    model = StockInfo
    serializer_class = StockInfoSerializer

    def get(self, request):
        stocks = ["amzn", "tsla", "goog", "meta", "nflx"]
        stocks = list(map(str.upper, stocks))
        fields = ["Open", "High", "Close", "Low"]

        df = yf.download(stocks, period="1wk")
        for index, row in df.iterrows():
            for name in stocks:
                val = StockInfo(name = name,
                                date = index,
                                open = row["Open", name],
                                high = row["High", name],
                                low = row["Low", name],
                                close = row["Close", name])
                val.save()

        output = [{"name": stock.name,
                   "date": stock.date,
                   "open": stock.open}
                  for stock in StockInfo.objects.all()]

        return JsonResponse(output, safe=False)

def index(r):
    return HttpResponse("haha")