from django.db import models

class Categoria (models.Model):
	nome = models.CharField(null = False , max_length = 255)
	salario = models.DecimalField(null = False , max_digits = 14 , decimal_places = 2)

	def __repr__(self):
		return 'Nome : %s   Salario : %s' % (self.nome , self.salario)

class Formacao (models.Model):
	nome = models.CharField(null = False , max_length = 255 , unique = True)

	def __repr__(self):
		return 'nome : %s' % (self.nome ,) 

class Professor(models.Model):
	nome = models.CharField(max_length = 255)
	cpf = models.CharField(unique= True , max_length = 11 , null = False)
	coordenador = models.BooleanField(default = False)
	formacao = models.ForeignKey(Formacao , related_name = id)
	categoria = models.ForeignKey(Categoria , related_name = id)

	def cpf_com_mascara(self):
		mascara = ''
		c = 0
		while c < len(self.cpf):
			if c == 3:
				mascara += '.'
			elif c == 6:
				mascara += '.'
			elif c == 9:
				mascara += '-'
			mascara += self.cpf[c]
			c += 1
		return mascara

	def salario_formatado(self):
		return str(self.categoria.salario).replace('.' , ',')