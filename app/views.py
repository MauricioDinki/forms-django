from .forms import DatosPersonalesForm,LoginForm
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView

# Formulario Usando FunctionView
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


# Ejemplo de Login Usando FormView
class LoginView(FormView):
	# Asignamos la plantilla html
	template_name = 'login-form.html'
	# Que formulario va a mostrar
	form_class = LoginForm
	# A  que url va a ir el el formulario si es valido
	success_url = '/success'

	# Si el formulario es valido, es lo mismo que form.is_valid() en el function view
	def form_valid(self,form):
		# logueamos al usuario por que ya comprobamos que existe y que su cuenta no esta inactiva el las validacones del forms.py, lo loguemos con la funcion login que hay que impirtar de django.contrib.auth
		login(self.request,form.user_cache)
		# llamamos al la funcion form_valid() para que nos redireccione a la url que ya definimos
		return super(LoginView,self).form_valid(form)


