# -*- coding:UTF-8 -*-
from django import forms
from professor.models import Formacao , Categoria
import psycopg2

#################################### CADASTRO PROFESSOR ##################################

class FormCadastroProfessor(forms.Form):
	nome = forms.CharField(required = True)
	cpf = forms.CharField(required = True)
	formacao = forms.ModelChoiceField(queryset=Formacao.objects.all())
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())


	def is_valid(self):
		valid = True
		if not super(FormCadastroProfessor , self).is_valid():
			self.adiciona_erro("Por favor verifique os dados informados")
			valid = False
		elif self.verifica_cpf(self.data['cpf']):
			self.adiciona_erro('O cpf já está cadastrado')
			valid = False
		return valid

	def adiciona_erro(self , mensagem):
		erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS , forms.utils.ErrorList())
		erros.append(mensagem)

	def verifica_cpf(self , cpf):
		con = psycopg2.connect(dbname= 'sistema_academico' , user= 'postgres' , password= '1234' , host= 'localhost')
		cursor = con.cursor()
		cursor.execute('SELECT COUNT(1) FROM professor_professor WHERE cpf = %s' , (cpf ,))
		if len(cursor.fetchall()) == 1:
			return False	
		return True

##################################### EDITAR PROFESSOR #####################################

class FormEditaProfessor(forms.Form):
	nome = forms.CharField(required= True)
	cpf = forms.CharField(required= True)
	formacao = forms.ModelChoiceField(queryset= Formacao.objects.all())
	categoria = forms.ModelChoiceField(queryset= Categoria.objects.all())

	


























