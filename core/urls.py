from django.urls import path
from .views import (
    HomeView, CreateProductView, UpdateProductView, DeleteProductView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', CreateProductView.as_view(), name='add'),
    path('edit/<int:pk>', UpdateProductView.as_view(), name='edit'),
    path('del/<int:pk>', DeleteProductView.as_view(), name='delete'),
]
