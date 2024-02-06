from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer
from .models import Product

# Create your views here.


class ListCreateProduct(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteProduct(APIView):
    def get(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs.get('id'))
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs.get('id'))
            serializer = ProductSerializer(product, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs.get('id'))
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)