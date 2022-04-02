from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('tabl/<str:nameTabl>/', def_list.as_view(), name='tabl'),  
    path('tabl/<str:nameTabl>/add', def_create_spr),
    path('tabl/<str:nameTabl>/<int:pk>', def_update_spr),
]