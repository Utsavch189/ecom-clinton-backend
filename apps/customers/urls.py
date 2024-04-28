from django.urls import path
from .views.address_views import *
from .views.user_views import *

urlpatterns=[
    path('address/',CustomerAddressAPI.as_view()),
    path('user/',CustomerAPI.as_view()),
]