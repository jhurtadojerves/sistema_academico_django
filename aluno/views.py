from django.shortcuts import render
from django.views.generic.base import View
from aluno.forms import CadastraAlunoForm , EditaAlunoForm
from aluno.models import Aluno

################################ cadastro aluno ###################################

def lista(request):
	return render(request , 'aluno_base.html')

class CadastrarAluno(View):

	def get(self , request):
		return render(request , 'cadastro_aluno.html')

	def post(self , request):
		form = CadastraAlunoForm(request.POST)
		if form.is_valid():
			dados = form.data
			aluno = Aluno(nome = dados['nome'] , data_nasc = dados['data_nasc'] , ano_entrada = dados['ano_entrada'] , cpf = dados['cpf'])
			aluno.save()
			return render(request , 'aluno_base.html')
		return render(request , 'cadastro_aluno.html' , {'form' : form})

############################### lista alunos ######################################

def lista_alunos(request):
	return render(request , 'lista_aluno.html' , {'alunos' : Aluno.objects.all()})

################################ edita aluno #######################################

class EditaAluno(View):
	
	def get(self , request , id_aluno):
		return render(request , 'editar_aluno.html' , {'aluno' : Aluno.objects.get(id=int(id_aluno))})

	def post(self , request , id_aluno):
		form = EditaAlunoForm(request.POST)
		if form.is_valid():
			dados = form.data
			aluno = Aluno.objects.get(id = int(id_aluno))
			aluno.nome = dados['nome']
			aluno.cpf = dados['cpf']
			aluno.data_nasc = dados['data_nasc']
			aluno.ano_entrada = dados['ano_entrada']
			if dados['ativo'] == 'true':
				aluno.ativo = True
			else:
				aluno.ativo = False
			aluno.save()
			return render(request , 'lista_aluno.html' , {'alunos' : Aluno.objects.all()})
		return render(request , 'editar_aluno.html' , {'form' : form})

#################################### REMOVE ALUNO ###################################

def remove_aluno(request , id_aluno):
	aluno = Aluno.objects.get(id = int(id_aluno))
	aluno.delete()
	return render(request , 'lista_aluno.html' , {'alunos' : Aluno.objects.all()})




