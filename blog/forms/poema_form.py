from django import forms
from ..models import Poema


class PoemaForm(forms.ModelForm):
    class Meta:
        model = Poema
        fields = ['titulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input input-bordered w-full '}),
            'imagen': forms.URLInput(attrs={'class': 'input input-bordered w-full '}),
        }


