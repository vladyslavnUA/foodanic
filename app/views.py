from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta

def home(request):
    context = {}
    return render(request, 'app/index.html', context)

def detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe': recipe,
    }
    return render(request, 'app/detail.html', context)

def create(request):
    context = {}
    if request.method == 'GET':
        form = RecipeForm()
        context['form'] = RecipeForm()
        return render(request, 'app/create.html', context)
    elif request.method == 'POST' and request.FILES != None:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new = Recipe()
            new.name = form['name'].value()
            new.description = form['description'].value()
            new.prep = form['prep'].value()
            new.cook = form['cook'].value()
            new.servings = form['servings'].value()
            new.ingredients = form['ingredients'].value()
            new.directions = form['directions'].value()
            new.notes = form['notes'].value()
            theimg = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(theimg.name, theimg)
            file_url = fs.url(filename)
            new.image = filename
            new.save()
            return redirect('home')
        else:
            form = RecipeForm()
            context['form'] = RecipeForm()
            return render(request, 'app/create.html', context)
    return render(request, 'app/create.html', context)

def update(request):
    context = {}
    return render(request, 'app/update.html', context)

def delete(request):
    context = {}
    return render(request, 'app/delete.html', context)