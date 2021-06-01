from django import forms
from django.forms import fields
from .models import cliente

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'
        