
from rest_framework import serializers
from Products.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'count']


class ProductSerializerv3(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_internal_value(self, data):
        internal_data = super.to_internal_value(data)
        print(internal_data['description'])
        internal_data['description'] = 'some description'
        return internal_data


    def to_representation(self, instance):
        result = super().to_representation(instance)
        del result['id']
        return result