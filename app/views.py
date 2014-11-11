from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import DatosPersonalesForm

def FormularioView(request):
	template = 'formulario.html'
	if request.method == 'POST': # Si el metodo es POST
		form = DatosPersonalesForm(request.POST) # Iniciamos EL Formulario
		if form.is_valid(): #Si Pasa todas las validaciones que definimos en el forms.py
			form = DatosPersonalesForm()
			return render_to_response(template, {'form':form,'success':'EL Formulario es Correcto'},context_instance=RequestContext(request))
	else: #Si el metodo es get solo mostramos el formulario
		form = DatosPersonalesForm()
	return render_to_response(template, {'form':form},context_instance=RequestContext(request))