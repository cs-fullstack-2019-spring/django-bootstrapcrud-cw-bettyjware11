from django import forms
from .models import GarbageSellModel


class GarbageSellForm(forms.ModelForm):
    class Meta:
        model = GarbageSellModel
        fields = "__all__"
