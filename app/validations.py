# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

# Mensajes de error
custom_error_messages = {
    'invalid_login': ('Usuario o password incorrectos'),
    'inactive': ('Su cuenta fue inhabilitada'),
    'null_field' : ('Este campo es requerido'),
    'blank_field': ('El campo esta en blanco'),
    'null_option':('Debes seleccionar una opcion'),
    'password_mismatch':('Las contraseñas no coinciden'),
    'user_exist':('Ese usuario ya esta ocupado'),
    'email_exist':('Ese email ya esta asociado una cuenta'),
}

def validate_null(data):
	if str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	return data

def validate_password(data_1,data_2):
	if len(str(data_2)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data_2).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data_1 and data_2 and data_1 != data_2:
		raise forms.ValidationError(custom_error_messages['password_mismatch'],)
	return data_2

def validate_username(data):
	if len(str(data)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data:
		try:
			user = User.objects.get(username = data)
		except User.DoesNotExist:
			return data
	raise forms.ValidationError(custom_error_messages['user_exist'],)

def validate_email(data):
	if len(str(data)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data:
		try:
			user = User.objects.get(email = data)
		except User.DoesNotExist:
			return data
	raise forms.ValidationError(custom_error_messages['email_exist'],)