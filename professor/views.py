from django.shortcuts import render
from django.views.generic.base import View
from professor.models import Formacao , Categoria , Professor
from professor.forms import FormCadastroProfessor , FormEditaProfessor

def lista_professores(request):
	return render(request , 'lista_professores.html' , {'lista_professores' : Professor.objects.all()})

######################################## CADASTRA PROFESSOR #################################

class CadastrarProfessor(View):
	def get(self , request):
		return render(request , 'cadastro_professor.html' , {'formacoes' : Formacao.objects.all() , 'categorias' : Categoria.objects.all()})

	def post(self , request):
		form = FormCadastroProfessor(request.POST)
		if form.is_valid():
			dados = form.data
			nome = dados['nome']
			cpf = dados['cpf']
			formacao = Formacao.objects.get(id = int(dados['formacao']))
			categoria = Categoria.objects.get(id = int(dados['categoria']))
			professor = Professor(nome = nome , cpf = cpf , formacao = formacao , categoria = categoria)
			professor.save()
			return render(request , 'lista_professores.html'  , {'lista_professores' : Professor.objects.all()})
		return render(request , 'cadastro_professor.html' , {'form' : form , 'formacoes' : Formacao.objects.all() , 'categorias' : Categoria.objects.all()})

####################################### EDITA PROFESSOR ####################################

class EditaProfessor(View):
	def get(self , request , id_professor):
		professor = pega_professor(id_professor)
		return render(request , 'edita_professor.html' , {'professor' : professor , 'formacoes' : Formacao.objects.all() , 'categorias' : Categoria.objects.all()})

	def post(self , request , id_professor):
		form = FormEditaProfessor(request.POST)
		dados = form.data
		professor = Professor.objects.get(id= id_professor)
		professor.nome = dados['nome']
		professor.cpf = dados['cpf']
		professor.formacao = Formacao.objects.get(id= dados['formacao'])
		professor.categoria = Categoria.objects.get(id= dados['categoria'])
		professor.save()
		return render(request , 'lista_professores.html', {'lista_professores' : Professor.objects.all()} )


def pega_professor(id_professor):
	return Professor.objects.get(id = int(id_professor))

def remove_professor(request , id_professor):
	professor = pega_professor(id_professor)
	professor.delete()
	return render(request , 'lista_professores.html' , {'lista_professores' : Professor.objects.all()})








