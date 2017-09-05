from django.shortcuts import render

# Create your views here.
def home(request):
	args = locals()

	return render(request, 'profiles/home.html', args)
	
