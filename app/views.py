from .forms import InformacionForm,LoginForm,RegisterForm
from django.contrib.auth import login
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView,TemplateView

# Formulario Usando FunctionView
def FormularioView(request):
	if request.method == 'POST': # Si el metodo es POST
		form = InformacionForm(request.POST) # Iniciamos EL Formulario
		if form.is_valid(): #Si Pasa todas las validaciones que definimos en el forms.py
			form = InformacionForm()
			return render_to_response('informacion-form.html', {'form':form,'success':'El Formulario es Correcto'},context_instance=RequestContext(request))
	else: #Si el metodo es get solo mostramos el formulario
		form = InformacionForm()
	return render_to_response('informacion-form.html', {'form':form},context_instance=RequestContext(request))

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

# Registro Usando FormView
class RegisterView(FormView):
	template_name = 'register-form.html'
	form_class = RegisterForm
	success_url = '/success'

	def form_valid(self,form):
		form.save()
		login(self.request,form.user_cache)
		return super(RegisterView,self).form_valid(form)

# Una forma rapida de mostrar una plantilla estatica es con un templateview solo le decimos el nombre de la plantilla 
class IndexView(TemplateView):
	template_name = "index.html"

class SuccessView(TemplateView):
	template_name = "success.html"

