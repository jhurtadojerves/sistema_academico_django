from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import CadastrarAluno , EditaAluno

urlpatterns = patterns('',
	url(r'^$' , 'aluno.views.lista') , 
	url(r'^/cadastro$' , CadastrarAluno.as_view() , name = "cadastro_aluno") ,
	url(r'^/lista$' , 'aluno.views.lista_alunos' , name = "lista_alunos") ,
	url(r'^/editar/(?P<id_aluno>\d+)$' , EditaAluno.as_view() , name="edita_aluno") ,
	url(r'^/remover/(?P<id_aluno>\d+)$' , 'aluno.views.remove_aluno' , name="remove_aluno") ,
	)
