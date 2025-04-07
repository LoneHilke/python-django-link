from django.shortcuts import render, redirect
from django.views import View
from .models import Python, Django, Link, Small

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/forside.html')
    
class PythonView(View):
    def get(self, request, *args, **kwargs):
        python = Python.objects.all()
        context = {
        'python': python,
        } 
        return render(request, 'app/python.html', context)
    
class DjangoView(View):
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
    
class Info(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/info.html')
    
class SmallView(View):
    def get(self, request, *args, **kwargs):
        small = Small.objects.all()
        context = {
        'small': small,
        } 
        return render(request, 'app/kode.html', context)
    
class Microsoft(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/m365.html')