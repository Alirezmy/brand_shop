from Products.serializers import ProductSerializerv3
from rest_framework import generics

from Products.models import Product


class ProductGenericsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerv3


