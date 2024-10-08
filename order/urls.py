from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('', views.orders_list, name='orders_list'),
    path('new/', views.new_order, name='new_order'),
    path('add/<str:phone>', views.add_order, name='add_order'),
]
