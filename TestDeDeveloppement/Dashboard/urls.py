from django.urls import path
from Dashboard.views import index

urlpatterns = [
    path('dashboard/', index),
]