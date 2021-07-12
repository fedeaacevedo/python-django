from django.forms import *

from core.erp.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Descripcion'
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            )


        }

