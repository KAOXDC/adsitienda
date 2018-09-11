from django.urls import path 
from .views import *
urlpatterns=[
	#path('',vista_inicio),
	path('about/',vista_about, name='about'),
	path('contacto/',vista_contacto, name='contacto'),
	path('lista_producto/', vista_lista_producto, name = 'lista_producto'),
	path('agregar_producto/', vista_agregar_producto, name='agregar_producto'),
	path('ver_producto/<int:id_prod>', vista_ver_producto, name = 'ver_producto'),
	path('editar_producto/<int:id_prod>', vista_editar_producto, name = 'editar_producto'),
	path('eliminar_producto/<int:id_prod>', vista_eliminar_producto, name = 'eliminar_producto'),

	path('crear_perfil/', vista_crear_perfil, name='crear_perfil'),
	
]