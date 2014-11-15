# -*- encoding: utf-8 -*-

from .models import Persona
from .validations import *
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import Field

# Mensajes de Error
default_error_messages = {
    'required': 'Este campo no puede estar vacio',
}

# Declaramos El Formulario
class InformacionForm(forms.Form):

	# Campo Nombre
	nombre = forms.CharField(
		# Hacemos que los mensajes de error sean los que definimos
		error_messages=default_error_messages,
		# Maxima lonngitud
        max_length=20,
        # Si es requerido
        required=True,
        # En el widget declaramos las clases del campo
        widget=forms.TextInput(attrs={'class' : 'block-center Info-input', 'placeholder':'Nombre'}),
    )

	# Select del Estado Civil
	estadoc = forms.ChoiceField(
		choices=(
			# El primer valor es su "value", el segundo es lo que se muestra en el html
			('', 'Estado Civil'),
		    ('SOL', 'Soltero'),
		    ('CAS', 'Casado'),
		    ('DIV', 'Divorciado'),
		    ('VIU', 'Viudo'),
		),
		error_messages=default_error_messages,
		required=True,
		widget=forms.Select(attrs={'class': 'block-center Info-select',}),
	)

	# Campo de comprobacion de humano
	es_humano = forms.BooleanField(
		error_messages=default_error_messages,
		required=True,
		widget=forms.CheckboxInput(attrs={'id':'checkbox','class':'css-checkbox lrg',}),
	)

	# Seleccion del deporte
	deporte = forms.ChoiceField(
		choices=(
			('Futbol', 'Futbol'),
			('Basquetball', 'Basquetball'),
			('Beisball', 'Beisball'),
		),
		error_messages=default_error_messages,
		required=True,
		widget=forms.RadioSelect(attrs={'class': 'Info-radio',}),
	)

	# Declaramos al Constructor
	def __init__(self, *args, **kwargs):
		super(InformacionForm, self).__init__(*args, **kwargs)
		# Si hay errores, va a recorrer todos los campos del formulario y por cada uno que encuentre con error, va a poner border-red a sus clases definidas
		if self.errors: 
		    for field in self.fields: 
		        if field in self.errors:
		        	# Si quereos remplazar todas las clases por otras, debemos comentar las siguientes 3 y descomentar la ultima 
		            classes = self.fields[field].widget.attrs.get('class', '')
		            classes += ' border-red'
		            self.fields[field].widget.attrs['class'] = classes

		            # self.fields[field].widget.attrs['class'] = 'nombre_de_la_clase'

    # Usaremos Funciones Para Validar Los Campos De Formulario
    # Las validaciones de cada campo deben de tener nombre clean_<nombre del campo>
	def clean_nombre(self):
		# Obtenemos el contenido de un campo del cleaned data y lo asignamos a una variable 
		nombre = self.cleaned_data.get('nombre')
		# Le enviamos el nombre a la funcion validate_null que esta en validations.py
		validate_null(nombre)
		# Siempre regresamos el valor que tomamos del cleaned_data
		return nombre

# Declaramos El Formulario
class LoginForm(forms.Form):

	# Campo Username
    username = forms.CharField(
		error_messages=default_error_messages,
    	max_length=20,
    	required=True,
    	widget=forms.TextInput(attrs={'class':'Login-input block-center','placeholder':'username'}),
    )

    # Campo Password
    password = forms.CharField(
		error_messages=default_error_messages,
    	max_length=20,
    	required=True,
    	# El widget debe ser PasswordInput para que aparescan los puntitos y no se va la contrasena
    	widget=forms.PasswordInput(attrs={'class':'Login-input block-center','placeholder':'password'}),
	)

    # Constructor
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # El user_cache es donde se almacena el usuario listo para loguear si pasa las validaciones
        self.user_cache = None
        if self.errors: 
		    for field in self.fields: 
		        if field in self.errors:
		            classes = self.fields[field].widget.attrs.get('class', '')
		            classes += ' border-red'
		            self.fields[field].widget.attrs['class'] = classes

    # Validamos El Username
    def clean_username(self):
		username = self.cleaned_data.get('username')
		validate_null(username)
		return username

	# Validamos el password
    def clean_password(self):
		password = self.cleaned_data.get('password')
		validate_null(password)
		return password

	# Es importante que la funcion se llame clean por que es la validacion general del formulario, y es aqui donde validamos que el usuario exista
    def clean(self):
    	# notese la diferencia de obtener el username del cleaned data, si lo hacemos de la foma self.cleaned_data[] va a mandar un KeyError
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Si hay password y username
        if username and password:
        	# en el user_cache que definimos en el constructor almacenamos el usuario que se autentifica con la funcion authenticate, que debemos importar de django.contrib.auth
            self.user_cache = authenticate(username=username, password=password)
            # Si no existe el usuario, user_cache estara vacio y mandamos el error
            if self.user_cache is None:
                raise forms.ValidationError(custom_error_messages['invalid_login'],)
            # Comprobamos que el Usuario este activo
            elif not self.user_cache.is_active:
                raise forms.ValidationError(custom_error_messages['inactive'])
        # Siempre regresamos el cleaned_data
        return self.cleaned_data
            
# Declaramos El Formulario
class RegisterForm(forms.Form):

	# Campo Username
	username = forms.CharField(
		# Con esto podemos cambiar los mensajes de error de las validaciones por defecto como required
		error_messages=default_error_messages,
    	max_length=20,
    	required=True,
    	widget=forms.TextInput(attrs={'placeholder':'Username'}),
    )

	# Campo Email
	email = forms.EmailField(
		error_messages={
			'invalid':('Ingresa una cuenta de correo valida'),
			'required': default_error_messages['required']
		},
		max_length=30,
		required=True,
		widget=forms.TextInput(attrs={'placeholder':'Email'}),
	)

	# Campo Nombre
	nombre = forms.CharField(
		error_messages=default_error_messages,
		max_length=20,
		required=True,
		widget=forms.TextInput(attrs={'placeholder':'Nombre'}),
	)

	# Campo Apellidos
	apellidos = forms.CharField(
		error_messages=default_error_messages,
		max_length=20,
		required=True,
		widget=forms.TextInput(attrs={'placeholder':'Apellidos'}),
	)

	# Campo Edad
	edad = forms.IntegerField(
		error_messages={
			'invalid':('La Edad Debe Ser Un Numero'),
			'required': default_error_messages['required']
		},
		required=True,
		widget=forms.TextInput(attrs={'placeholder':'Edad'}),
	)

	# Campo Password
	password_1 = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=True,
		widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}),
	)

	# Campo De Comprobacion de Password
	password_2 = forms.CharField(
		error_messages=default_error_messages,
		max_length=30,
		required=True,
		widget=forms.PasswordInput(attrs={'placeholder':'Repetir Contraseña'}),
	)

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.user_cache = None
		if self.errors: 
		    for field in self.fields: 
		        if field in self.errors:
		            classes = self.fields[field].widget.attrs.get('class', '')
		            classes += ' border-red'
		            self.fields[field].widget.attrs['class'] = classes


	def clean_apellidos(self):
		apellidos = self.cleaned_data.get('apellidos')
		validate_null(apellidos)
		return apellidos

	def clean_edad(self):
		edad = self.cleaned_data.get('edad')
		validate_null(edad)
		return edad

	def clean_email(self):
		email = self.cleaned_data.get('email')
		validate_email(email)
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get('nombre')
		validate_null(nombre)
		return nombre

	def clean_password_1(self):
		password_1 = self.cleaned_data.get('password_1')
		validate_null(password_1)
		return password_1

	def clean_password_2(self):
		password_1 = self.cleaned_data.get('password_1')
		password_2 = self.cleaned_data.get("password_2")
		validate_password(password_1,password_2)
		return password_1 and password_2

	def clean_username(self):
		username = self.cleaned_data.get('username')
		validate_username(username)
		return username

	def save(self):
		# Obtenemos los datos del Formulario
		username = self.cleaned_data.get("username")
		email = self.cleaned_data.get("email")
		password = self.cleaned_data.get("password_2")
		nombre = self.cleaned_data.get("nombre")
		apellidos = self.cleaned_data.get("apellidos")
		edad = self.cleaned_data.get("edad")

		# Creamos El Usuario
		user = User.objects.create_user(username, email, password)
		user.first_name = nombre
		user.last_name = apellidos
		user.save()

		# Añadimos al modelo Persona nuestro Usuario
		newPersona = Persona(user=user,edad=edad )
		newPersona.save()

		# Lo autentificamos y no tenemos que validar que existe por que lo acabamos de registrar
		self.user_cache = authenticate(username=username, password=password)