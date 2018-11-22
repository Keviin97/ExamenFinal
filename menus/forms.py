from django import forms

from .models import Plato, Menu


class MenuForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Menu
        fields = ('nombre', 'descripcion', 'total' ,'platillos')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
def __init__ (self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields["platillos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["platillos"].help_text = "Ingrese los platillos que integran el menu"
        self.fields["platillos"].queryset = Actor.objects.all()