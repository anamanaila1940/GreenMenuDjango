from django.forms import ModelForm
from items.models import *

class MistakeForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','mistakeprice','quantity','mistake']