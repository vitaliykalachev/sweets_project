from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recipes

# Create your views here.

def index(request):
    recipes = Recipes.objects,all().values()
    template = loader.get_template('home.html')
    
    context = {
        'recipes': recipes,
    }
    
    return HttpResponse(template.render({}, request))
    
    