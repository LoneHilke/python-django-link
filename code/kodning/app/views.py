from django.shortcuts import render, redirect
from django.views import View
from .models import Python, Django, Link

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/forside.html')
    
class Python(View):
    def get(self, request, *args, **kwargs):
        python = Python.objects.all()
        context = {
        
        'python': python,
      } 
        return render(request, 'app/python.html', context)
    
class Django(View):
    def get(self, request, *args, **kwargs):
        django = Django.objects.all()
        context ={
            'django':django
        }
        return render(request, 'app/django.html', context)
    
class Deploy(View):
    def get(self, request, *args, **kwargs):
        link = Link.objects.all()
        context = {
            'link':link
        }
        return render(request, 'app/deploy.html', context)
    
class Terminals(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/terminals.html')