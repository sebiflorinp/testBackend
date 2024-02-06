from rest_framework.urls import path
from .views import ListCreateProduct


urlpatterns = [
    path('products', ListCreateProduct.as_view(), name='list_create_product')
]