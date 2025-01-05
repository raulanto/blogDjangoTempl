from django import forms

from ..models import LineaTiempo


class LineaTiempoForm(forms.ModelForm):
    class Meta:
        model = LineaTiempo
        fields = ['titulo', 'contenido', 'fecha']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input input-bordered w-full '}),
            'contenido': forms.Textarea(attrs={'class': 'input input-bordered w-full ', 'rows': 5}),
            'fecha': forms.TextInput(attrs={'class': 'input input-bordered w-full ','type':'date'}),
        }
