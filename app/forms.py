from django import forms
from django.contrib.auth import authenticate

# Mensajes de Error
error_messages = {
    'invalid_login': ('Usuario o password incorrectos'),
    'inactive': ('Su cuenta fue inhabilitada'),
    'null_field' : ('Este campo es requerido'),
    'blank_field': ('El campo esta en blanco'),
    'null_option':('Debes seleccionar una opcion')
}

# Declaramos El Formulario
class InformacionForm(forms.Form):

	# Campo Nombre
	nombre = forms.CharField(
        max_length=30,
        # En el widget declaramos las clases del campo
        widget=forms.TextInput(attrs={'class' : 'block-center Info-input', 'placeholder':'Nombre'}),
        required=False,
    )

	# Select del Estado Civil
	estadoc = forms.ChoiceField(
		required=False,
		widget=forms.Select(attrs={'class': 'block-center Info-select',}),
		choices=(
			# El primer valor es su "value", el segundo es lo que se muestra en el html
			('', 'Estado Civil'),
		    ('SOL', 'Soltero'),
		    ('CAS', 'Casado'),
		    ('DIV', 'Divorciado'),
		    ('VIU', 'Viudo'),
		),
	)
	es_humano = forms.BooleanField(
		widget=forms.CheckboxInput(attrs={'id':'checkbox','class':'css-checkbox lrg',}),
	)

	deporte = forms.ChoiceField(
		required=False,
		widget=forms.RadioSelect(attrs={'class': 'Info-radio',}),
		choices=(
			('Futbol', 'Futbol'),
		    ('Basquetball', 'Basquetball'),
		    ('Beisball', 'Beisball'),
		),
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

	def clean_nombre(self):
		# Obtenemos El Contenido de un campo del cleaned data y lo asignamos a una variable 
		nombre = self.cleaned_data['nombre']
		# Validamos que el Campo No este Vacio
		if len(nombre) == 0:
			# Si esta vacio levantamos un error de validacion
			raise forms.ValidationError(error_messages['null_field'],)
		# Si el campo solo tiene espacios en blanco
		elif nombre.isspace():
			raise forms.ValidationError(error_messages['blank_field'],)
		return nombre
		# Siempre regresamos el valor del campo

	def clean_estadoc(self):
		estadoc = self.cleaned_data["estadoc"]
		if len(estadoc) == 0: #La Opcion Estado Civil No Tiene Valor
			raise forms.ValidationError(error_messages['null_option'],)
		return estadoc

	def clean_es_humano(self):
		es_humano = self.cleaned_data["es_humano"]
		if not es_humano:
			raise forms.ValidationError(error_messages['null_option'],)
		return es_humano

	def clean_deporte(self):
		deporte = self.cleaned_data["deporte"]
		if not deporte:
			raise forms.ValidationError(error_messages['null_option'],)
		return deporte

# Declaramos El Formulario
class LoginForm(forms.Form):

	# Campo Username
    username = forms.CharField(
    	required=False,
    	max_length=30,
    	widget=forms.TextInput(attrs={'class':'Login-input block-center','placeholder':'username'}),
    )

    # Campo Password
    password = forms.CharField(
    	required=False,
    	max_length=30,
    	# El widget debe ser PasswordInput para que aparescan los puntitos y no se va la contrasena
    	widget=forms.PasswordInput(attrs={'class':'Login-input block-center','placeholder':'password'}),
	)

    # Constructor
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # El user_cache es donde se almacena el usuario listo para loguear si pasa las validaciones
        self.user_cache = None
        # Para poner una clase extra a los campos
        if self.errors: 
		    for field in self.fields: 
		        if field in self.errors:
		            classes = self.fields[field].widget.attrs.get('class', '')
		            classes += ' border-red'
		            self.fields[field].widget.attrs['class'] = classes

    # Validamos El Username
    def clean_username(self):
		username = self.cleaned_data['username']
		if len(username) == 0:
			raise forms.ValidationError(error_messages['null_field'],)
		elif username.isspace():
			raise forms.ValidationError(error_messages['blank_field'],)
		return username

	# Validamos el password
    def clean_password(self):
		password = self.cleaned_data['password']
		if len(password) == 0:
			raise forms.ValidationError(error_messages['null_field'],)
		elif password.isspace():
			raise forms.ValidationError(error_messages['blank_field'],)
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
                raise forms.ValidationError(error_messages['invalid_login'],)
            # Comprobamos que el Usuario este activo
            elif not self.user_cache.is_active:
                raise forms.ValidationError(error_messages['inactive'])
        # Siempre regresamos el cleaned_data
        return self.cleaned_data
            


	