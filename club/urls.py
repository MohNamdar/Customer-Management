from django.urls import path
from . import views

app_name = 'club'
urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.customers_list, name='customers_list'),
]
