from django.urls import path
from .views import ProductAPI

urlpatterns=[
    path('',ProductAPI.as_view())
]