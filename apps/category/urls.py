from django.urls import path
from .views import *

urlpatterns=[
    path('',CategoryAPI.as_view())
]