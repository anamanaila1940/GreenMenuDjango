from django.forms import ModelForm
from items.models import *

class LocalGoodsForm(ModelForm):
    class Meta:
        model = LocalGoods
        fields = '__all__'