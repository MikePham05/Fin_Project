from django.urls import path
from .views import StockInfoView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stock/", StockInfoView.as_view(), name="basic stock info display")
]