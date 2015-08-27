# -*- coding:UTF-8 -*-
from django import forms
import psycopg2

################################### cadastra aluno ###################################

class CadastraAlunoForm(forms.Form):
	nome = forms.CharField(required = True)
	cpf = forms.CharField(required = True)
	data_nasc = forms.CharField(required = True)
	ano_entrada = forms.CharField(required = True)

	def is_valid(self):
		valid = True
		if not super(CadastraAlunoForm , self).is_valid():
			self.adiciona_erro("Por favor verifique os dados informados")
			valid = False
		elif self.verifica_registro(self.data['cpf']):
			self.adiciona_erro("Cpf já está cadastrado")
			valid = False
		return valid

	def adiciona_erro(self , mensagem):
		erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS , forms.utils.ErrorList())
		erros.append(mensagem)

	def verifica_registro(self , cpf):
		con = psycopg2.connect(dbname = "sistema_academico" , user = 'postgres' , password = '1234' , host = 'localhost')
		cursor = con.cursor()
		cursor.execute('SELECT 1 FROM aluno_aluno WHERE cpf = %s' , (cpf , ))
		result = cursor.fetchall()
		cursor.close()
		con.close()
		if len(result) == 1:
			return True
		return False

##################################### EDITA ALUNO #######################################

class EditaAlunoForm(forms.Form):
	nome = forms.CharField(required = True)
	cpf = forms.CharField(required = True)
	data_nasc = forms.CharField(required = True)
	ano_entrada = forms.CharField(required = True)
	ativo = forms.RadioSelect()
	id = forms.CharField(required = True)
	
	def is_valid(self):	
		valid = True
		if not super(EditaAlunoForm , self).is_valid():
			self.adiciona_erro("Por favor verifique os dados informados")
			valid = False
		return valid


	def adiciona_erro(self , mensagem):
		erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS , forms.utils.ErrorList())
		erros.append(mensagem)

	def verifica_registro(self , cpf):
		con = psycopg2.connect(dbname = "sistema_academico" , user = 'postgres' , password = '1234' , host = 'localhost')
		cursor = con.cursor()
		cursor.execute('SELECT 1 FROM aluno_aluno WHERE cpf = %s' , (cpf , ))
		result = cursor.fetchall()
		cursor.close()
		con.close()
		if len(result) == 1:
			return True
		return False











