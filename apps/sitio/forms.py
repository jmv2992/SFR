from django import forms
from .models import Cliente


class FormCliente(forms.Form):
    nombre = forms.CharField(label='<b>Name prisss</b>', max_length=200)
    empresa = forms.CharField(label='<b>Name empresa prisss</b>', max_length=200, required=False)
    mensaje = forms.CharField(label='<b>Mensaje</b>', widget=forms.Textarea)
    telefono = forms.CharField(label='<b>Telefono</b>', max_length=200)
    email = forms.EmailField(label='<b>E-mail</b>', max_length=200)

    def save(self):
        data = self.cleaned_data
        cli = Cliente(nombre=data['nombre'], empresa=data['empresa'], mensaje=data['mensaje'],
                      telefono=data['telefono'], email=data['email'])
        cli.save()
