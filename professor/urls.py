from django.conf.urls import patterns, url
from professor.views import CadastrarProfessor , EditaProfessor

urlpatterns = patterns('',
	url(r'^$' , 'professor.views.lista_professores' , name = 'lista_professores') ,
	url(r'^/cadastro$' , CadastrarProfessor.as_view() , name = 'cadastro_professor') ,
	url(r'^/edita/(?P<id_professor>\d+)' , EditaProfessor.as_view() , name= 'edita_professor') ,
	url(r'^/remove/(?P<id_professor>\d+)' , 'professor.views.remove_professor' , name= 'remove_professor') ,	
	)