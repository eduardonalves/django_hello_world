from django.db import models

# Create your models here.
class CourseManager(object):
	"""docstring for ClassName"""
	def search(self, query):
		return self.get_queryset().filter(
			name_icontains = query, description_icontains= query
		)

class Course(models.Model):
	name = models.CharField('Nome', max_length=255)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descricao Simples', blank=True)
	about = models.TextField('Sobre o Curso', blank=True)	
	start_date = models.DateField(
		'Data Início', null = True, blank= True
	)
	image = models.ImageField(
		upload_to = 'images/courses', verbose_name='Imagem', null=True, blank=True
	)
	created_at = models.DateTimeField(
		'Criado em', auto_now_add = True
	)
	updated_at = models.DateTimeField(
		'Atualizado em', auto_now = True
	)
	def __str__(self):
		return self.name

	#@models.permalink
	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('details', kwargs={'slug': self.slug})
		#caso queira retornar a url por id ao invés do slug
		#return reverse('details', kwargs={'id': self.pk})
	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		#ordering = ['-name'] ordenado desc
		ordering = ['name'] #ordenado por nome crescente
		
			
	
		