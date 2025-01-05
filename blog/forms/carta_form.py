from django import forms

from ..models import Carta


class CartaForm(forms.ModelForm):
    class Meta:
        model = Carta
        fields = ['titulo', 'destinatario', 'contenido', 'posdata', 'imagen', 'iframe']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input input-bordered w-full '}),
            'destinatario':forms.Select(attrs={'class': 'select select-bordered w-full '}),

            'posdata': forms.Textarea(attrs={'class': 'input input-bordered w-full '}),
            'imagen': forms.URLInput(attrs={'class': 'input input-bordered w-full '}),
            'iframe': forms.Textarea(attrs={'class': 'input input-bordered w-full '}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Extraemos el usuario pasado como argumento
        super().__init__(*args, **kwargs)
        # Filtramos los usuarios para excluir al usuario logueado
        self.fields['destinatario'].queryset = self.fields['destinatario'].queryset.exclude(id=user.id)