from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, max_length= 70)
    email = forms.EmailField(label="Correo Electronico", required=True)
    contenido = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea)