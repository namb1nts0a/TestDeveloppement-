from django.urls import path
from Login.views import login, signup


urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup)
]