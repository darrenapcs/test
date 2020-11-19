from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})
	#return HttpResponse("<h1>Hello User</h1>")

def contact_view(*args, **kwargs):
	return HttpResponse("<h1>Contact Page</h1>")

def connect_view(*args, **kwargs):
	return HttpResponse("<h1>Connect Page</h1>")
