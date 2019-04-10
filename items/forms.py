from items.models import Item
from django.forms import ModelForm


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'photo']
