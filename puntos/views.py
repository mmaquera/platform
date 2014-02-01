from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView
from .models import Persona
from .forms import PersonaForm
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy

class RegistrarMiembro(CreateView):
	template_name = 'registrar_miembro.html'
	model = Persona
	success_url = reverse_lazy('listar_miembros')

class ListarMiembros(ListView):
	template_name = 'listar_miembros.html'
	model = Persona

def dashboard(request):
	template_name = 'dashboard.html'
	return render_to_response(template_name,context_instance=RequestContext(request,locals()))

def miembro(request):
	template_name = 'miembro.html'
	miembro = Persona.objects.all()
	dic = {'miembro' : miembro }
	return render_to_response(template_name, dic, context_instance=RequestContext(request,locals()))

def editar_miembro(request):
	template_name = 'editar_miembro.html'
	key_dni = request.GET.get('dni')
	miembro = Persona.objects.filter(dni = key_dni)
	dic = {'miembro' : miembro }
	return render_to_response(template_name, dic, context_instance=RequestContext(request,locals()))

def agregar_miembro(request):
	estado = False
	template_name = 'agregar_miembro.html'

	if request.method == "POST":
		form = PersonaForm(request.POST)
		if form.is_valid():
			persona = form.save(commit=False)
			persona.usuario_new = request.user
			persona.save()
			estado = True
			dic = { 'estado' : estado }
			return render_to_response(template_name, dic, context_instance=RequestContext(request,locals()))
	else:
		form = PersonaForm()

	return render_to_response(template_name,context_instance=RequestContext(request,locals()))

def puntaje(request):
	template_name = 'puntaje.html'
	return render_to_response(template_name,context_instance=RequestContext(request,locals()))

def regla(request):
	template_name = 'regla.html'
	return render_to_response(template_name,context_instance=RequestContext(request,locals()))

def cargo(request):
	template_name = 'cargo.html'
	return render_to_response(template_name,context_instance=RequestContext(request,locals()))		

def historico(request):
	template_name = 'historico.html'
	return render_to_response(template_name,context_instance=RequestContext(request,locals()))

def recompensa(request):
	template_name = 'recompensa.html'
	return render_to_response(template_name,context_instance=RequestContext(request,locals()))

def tarjeta(request):
	template_name = 'tarjeta.html'
	return render_to_response(template_name,context_instance=RequestContext(request,locals()))