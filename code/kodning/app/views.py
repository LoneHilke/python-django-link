from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/forside.html')
    
class Python(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/python.html')
    
class Django(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/django.html')