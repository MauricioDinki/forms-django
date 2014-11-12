from django import forms

# Iniciamos Un formulario normal
class DatosPersonalesForm(forms.Form):
	# Campos de Formulario Normales 
	nombre = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class' : 'Input-Text', 'placeholder':'Nombre'}), #Especificamos la clase css cuando el campo este normal
        required=False,
    )

	estadoc = forms.ChoiceField(
		required=False,
		widget=forms.Select(attrs={'class': 'Input-Select',}),
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
		widget=forms.CheckboxInput(attrs={'id': 'es_humano',}),

	)

	deporte = forms.ChoiceField(
		required=False,
		widget=forms.RadioSelect(attrs={'class': 'Normal',}),
		choices=(
			('Futbol', 'Futbol'),
		    ('Basquetball', 'Basquetball'),
		    ('Beisball', 'Beisball'),
		),
	)

	# Declaramos al Constructor
	def __init__(self, *args, **kwargs):
		super(DatosPersonalesForm, self).__init__(*args, **kwargs)
		# Si hay errores, va a recorrer todos los campos del formularioy por cada uno que encuentre con error, va a 
		# Sustituir su clase en este caso Normal, Por la clase Error
		if self.errors: 
		    for field in self.fields: 
		        if field in self.errors:
		        	# Si quereos remplazar todas las clases por otras, debemos comentar las siguientes 3 y descomentar la ultima 

		            classes = self.fields[field].widget.attrs.get('class', '')
		            classes += ' Error-Border'
		            self.fields[field].widget.attrs['class'] = classes

		            # self.fields[field].widget.attrs['class'] = 'Error'

    # Usaremos Funciones Para Validar LOs Campos De Formulario

	def clean_nombre(self):
		# Obtenemos El Contenido de un campo del cleaned data y lo asignamos a una variable 
		nombre = self.cleaned_data['nombre']
		# Validamos que el Campo No este Vacio
		if len(nombre) == 0:
			# Si esta vacio levantamos un error de validacion
			raise forms.ValidationError("Ingresa Tu Nombre")
			# Si el campo solo tiene espacios en blanco
		elif nombre.isspace():
			raise forms.ValidationError("Tu Nombre esta En Blanco")
		return nombre
		# Si todo es correcto regresamos el nombre

	def clean_estadoc(self):
		estadoc = self.cleaned_data["estadoc"]
		if len(estadoc) == 0: #La Opcion Estado Civil No Tiene Valor
			raise forms.ValidationError("Selecciona Un Estado Civil")
		return estadoc

	def clean_es_humano(self):
		es_humano = self.cleaned_data["es_humano"]
		if not es_humano:
			raise forms.ValidationError("No Eres Humano")
		return es_humano

	def clean_deporte(self):
		deporte = self.cleaned_data["deporte"]
		if not deporte:
			raise forms.ValidationError("Selecciona Un Deporte")
		return deporte
		