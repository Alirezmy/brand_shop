from django.forms import ModelForm
from Products.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'