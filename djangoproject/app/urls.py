from django.urls import path
from app.views import home, testpage

urlpatterns = [
    path('', home),
    path('test/', testpage),
]