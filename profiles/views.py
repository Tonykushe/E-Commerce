from django.shortcuts import render
from profiles.forms import *
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
	args = locals()

	return render(request, 'profiles/home.html', args)
	
def about(request):
	args = locals()

	return render(request, 'profiles/about.html', args)

def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Message from MYSITE.com'
		message = '%s %s' %(name, comment)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)

		title = 'Thanks'
		confirm_message = 'Message Sent! We will get back to you shortly.'
		form = None

	context = {'title': title, 'form': form, 'confirm_message': confirm_message}		
	return render(request, 'profiles/contact.html', context)
	
