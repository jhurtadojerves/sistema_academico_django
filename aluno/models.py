from django.db import models

class Aluno(models.Model):
	nome = models.CharField(max_length = 255 , null = False)
	data_nasc = models.CharField(max_length = 10 , null = False )
	ativo = models.BooleanField(default = True)
	ano_entrada = models.CharField(max_length = 6 , null = False)
	cpf = models.CharField(max_length = 11 , null = False , unique = True)

	def __str__(self):
		return 'Nome : %s - Data nasc : %s - Ano entrada : %s - Cpf : %s - Ativo : %s' % (self.nome , self.data_nasc , self.ano_entrada , self.cpf , self.ativo)

	@property
	def cpf_com_mascara(self):
		mascara = ''
		indice = 0
		while indice < 11:
			if indice == 3:
				mascara += '.'
			elif indice == 6:
				mascara += '.'
			elif indice == 9:
				mascara += '-'
			mascara += self.cpf[indice]
			indice += 1
		return mascara