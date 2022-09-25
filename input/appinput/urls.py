from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='main'),
    path('data/', Data.as_view(), name='data'),

]
