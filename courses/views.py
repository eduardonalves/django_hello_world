from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse
# Create your views here.
def index(request):
	courses = Course.objects.all()
	template_name = 'index.html'
	context = {
		'courses': courses,
	}
	return render(request, template_name, context)

def courses(request):
	template_name = 'index.html'
	return render(request, template_name)

def duvidas(request):
	template_name = 'duvidas.html'
	return render(request, template_name)


# def details(request, id):
# 	template_name = 'details.html'
# 	#course = Course.objects.get(pk=id)
# 	course = get_object_or_404(Course, pk=id)
# 	context = {
# 		'course': course
# 	}
# 	return render(request, template_name, context) 

def details(request, slug):
	template_name = 'details.html'
	#course = Course.objects.get(pk=id)
	course = get_object_or_404(Course, slug=slug)
	context = {}
	#se for post salva a duvida do formulario de contato do curso
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			#acessando determinado campo do formulario
			#print(form.cleaned_data['name'])
			#print(form.cleaned_data['message'])
			#zerar o form
			#form = ContactCourse()
			form.send_email(course)
	else:
		form = ContactCourse()
	context['form'] = form
	context['course'] = course

	return render(request, template_name, context) 