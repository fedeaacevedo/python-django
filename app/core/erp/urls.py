from django.urls import path
from core.erp.views import index, segunda_vista
urlpatterns = [
    path('uno/', index),
    path('second_view/', segunda_vista)
]