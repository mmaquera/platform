from django.conf.urls import patterns, include, url
from .views import *
from django.conf import settings

urlpatterns = patterns('',
	url(r'^registrar/$', RegistrarMiembro.as_view(), name='registrar_miembro'),
	url(r'^listar/', ListarMiembros.as_view(), name='listar_miembros'),
	
	url(r'^dashboard/', 'puntos.views.dashboard', name='dashboard'),
	
	url(r'^miembro/', 'puntos.views.miembro', name='miembro'),
	url(r'^editar_miembro/', 'puntos.views.editar_miembro', name='editar_miembro'),
	url(r'^agregar_miembro/', 'puntos.views.agregar_miembro', name='agregar_miembro'),
	
	url(r'^puntaje/', 'puntos.views.puntaje', name='puntaje'),
	url(r'^regla/', 'puntos.views.regla', name='regla'),
	url(r'^cargo/', 'puntos.views.cargo', name='cargo'),
	url(r'^historico/', 'puntos.views.historico', name='historico'),
	url(r'^recompensa/', 'puntos.views.recompensa', name='recompensa'),
	url(r'^tarjeta/', 'puntos.views.tarjeta', name='tarjeta'),
	
	
)
