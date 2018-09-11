from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def vista_about(request):
	nombre = ["Diego Prado","Diego 2"]
	#return render(request,'about.html', {'nombresito':nombre})
	return render(request,'about.html', locals())

def vista_contacto(request):
	formulario = contacto_form()
	return render(request, 'contacto.html', locals())

def vista_lista_producto(request):
	productos = Producto.objects.all()
	return render(request, 'lista_producto.html', locals())

def vista_agregar_producto(request):
	if request.method == "POST":
		formulario = agregar_producto_form(request.POST, request.FILES)
		if  formulario.is_valid():
			formulario.save()
		return redirect('/lista_producto/') 
	else: # entonces es un metodo GET
		formulario = agregar_producto_form()
	return render(request, 'agregar_producto.html', locals())

def vista_ver_producto(request, id_prod):

	p = Producto.objects.get(id = id_prod)
	
	return render(request,'ver_producto.html', locals())

def vista_editar_producto(request, id_prod):
	pro = Producto.objects.get(id = id_prod)
	#SELECT * from home_producto WHERE id == id_prod;
	formulario = agregar_producto_form(instance = pro)
	if request.method == "POST":
		formulario = agregar_producto_form(request.POST, instance = pro)
		formulario.save()
		msj = "se guardaron los cambios con exito"
	return render(request,'agregar_producto.html', locals())
	

def vista_eliminar_producto(request, id_prod):
	pro = Producto.objects.get(id = id_prod)
	pro.delete()
	return redirect('/lista_producto/')

def vista_crear_perfil (request):
	form_1 = register_form()
	form_2 = perfil_form()
	if request.method=='POST':
		form_1 = register_form(request.POST)
		form_2 = perfil_form(request.POST, request.FILES)
		if form_1.is_valid() and form_2.is_valid():
			usuario 	= form_1.cleaned_data['username']
			correo 		= form_1.cleaned_data['email']
			password_1 	= form_1.cleaned_data['password_1']
			password_2 	= form_1.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			
			y = form_2.save(commit=False)
			y.user= u
			y.save()
			msg = "gracias por registrarse..."

	return render(request,'crear_perfil.html', locals())

