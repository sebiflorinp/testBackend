from rest_framework.urls import path
from .views import ListCreateProduct, RetrieveUpdateDeleteProduct


urlpatterns = [
    path('products', ListCreateProduct.as_view(), name='list_create_product'),
    path('product/<int:id>', RetrieveUpdateDeleteProduct.as_view(), name='retrieve_update_delete_product')
]