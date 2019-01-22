from django.contrib import admin
from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'start_date','created_at']
	search_fields = ['name','slug', 'start_date']
	prepopulated_fields = {'slug': ['name']} #pré popula ou autocompleta o campo slug na tela de cadastro

admin.site.register(Course, CourseAdmin)