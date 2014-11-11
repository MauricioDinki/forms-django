from django import forms

# Iniciamos Un formulario normal
class DatosPersonalesForm(forms.Form):
	# Campos de Formulario Normales 
	nombre = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class' : 'Normal'}), #Especificamos la clase css cuando el campo este normal
        required=False,
    )

	# Declaramos al Constructor
	def __init__(self, *args, **kwargs):
		super(DatosPersonalesForm, self).__init__(*args, **kwargs)
		# Si hay errores, va a recorrer todos los campos del formularioy por cada uno que encuentre con error, va a 
		# Sustituir su clase en este caso Normal, Por la clase Error
		if self.errors: 
		    for field in self.fields: 
		        if field in self.errors:
		        	# Si no queremos sustituir la clase, sino agregar una clase error debemos comentar la ultima linea
		        	# y descomentar las siguinetes 3, solo va a obtener la/s clases de ese campo, lo suarda en la 
		        	# Variable "classes", le agrega una clase Error y vuelve a asignar el atributo class al campo

		            #classes = self.fields[field].widget.attrs.get('class', '')
		            #classes += ' Error'
		            # self.fields[field].widget.attrs['class'] = classes

		            self.fields[field].widget.attrs['class'] = 'Error'

    # Usaremos Funciones Para Validar LOs Campos De Formulario

	def clean_nombre(self):
		# Obtenemos El Contenido de un campo del cleaned data y lo asignamos a una variable 
		nombre = self.cleaned_data['nombre']
		# Validamos que el Campo No este Vacio
		if len(nombre) == 0:
			# Si esta vacio levantamos un error de validacion
			raise forms.ValidationError("El Campo No Puede Estar Vacio")
			# Si el campo solo tiene espacios en blanco
		elif nombre.isspace():
			raise forms.ValidationError("El Campo No Puede Contener Solo Espacios en Blanco")
		# Si todo es correcto regresamos el nombre
		return nombre
