from django import forms
from django.forms import ModelForm
from models import *

class PersonaForm(ModelForm):
	class Meta:
		model = Persona
		exclude = ("usuario_new", "usuario_mod", "fecha_new", "fecha_mod",)