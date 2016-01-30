from django import template
from academicManager import models

'''#Carrega o registro de template tags
register = template.Library()

#Registra o metodo a seguir como uma inclusion_tag indicando o template a ser renderizad
@register.inclusion_tag('alunos_n_cadastrados.html')
def alunos_n_cadastrados():
	alunos = models.Aluno.objects.order_by('data_nascimento')[0:5]
	return { 'alunos' : alunos }'''
