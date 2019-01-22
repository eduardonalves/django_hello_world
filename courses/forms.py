from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template

class ContactCourse(forms.Form):
	"""docstring for ContactCourse"""
	name = forms.CharField(label='Nome', max_length=111)
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea, required=False)

	def send_email(self, course):
		subject = 'Contato sobre o curso %s' % course
		message = 'Nome: %(name)s; E-mail: %(email)s; %(message) s'
		context = {
			'name': self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'message': self.cleaned_data['message']
		}
		message = message % context
		#send_email(subject, message, settings.DEFAULT_FROM_EMAIL ,[settings.CONTACT_EMAIL] )
		template_name = 'contact_email.html'
		send_email_template(
			subject, template_name, context, [settings.CONTACT_EMAIL]
		)
