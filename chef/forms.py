from django.forms import ModelForm
from items.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','status','price']