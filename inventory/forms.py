from django.forms import ModelForm
from .models import InventoryPost

class InventoryPostForm(ModelForm):
    class Meta:
        model = InventoryPost
        fields = ["category", "title", "comment", "image1", "image2"]