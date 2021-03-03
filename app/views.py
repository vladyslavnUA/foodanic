from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta
from markdownx.utils import markdownify
from .models import *
from .forms import *
from django.contrib.auth.decorators import user_passes_test

def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'app/index.html', context)

def detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.ingredients = markdownify(recipe.ingredients)
    recipe.directions = markdownify(recipe.directions)

    context = {
        'recipe': recipe,
    }
    return render(request, 'app/detail.html', context)

@login_required
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
            user = request.user
            new.author = user
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

@login_required
def update(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe': recipe
    }
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context['form'] = form
        return render(request, 'app/update.html', context)
    elif request.method == 'POST' and request.FILES != None:
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('detail', recipe.id)
        else:
            form = RecipeForm(instance=recipe)
            context['form'] = form
            return render(request, 'app/update.html', context)
    return render(request, 'app/update.html', context)

@login_required
def delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if not request.user == recipe.author:
        return redirect('detail', recipe.id)
    else:
        name = recipe.name
        recipe.delete()
        context = {
            'name': name
        }
        return render(request, 'app/delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def load(request):
    # 🧀🥞🥪🌮🥗
    new = Recipe.objects.create(name='Pizza', description='Italian-styled home-made dough recipe along with instructions on how to turn it into pizza 🍕',
                                prep='0:30:00', cook='1:30:00', servings=2, image='media/image_lHvewhO.jpg', ingredients='Sample list of ingredients', 
                                directions='''## Step 1 
something here
## Step 2 
something else here
## Step 3
last step''', notes='', author=request.user)
    new.save()
    new1 = Recipe.objects.create(name='Cheese', description='Some sample cheese recipe 🧀',
                                prep='0:45:00', cook='2:00:00', servings=5, image='media/square.jpg', ingredients='Sample list of ingredients', 
                                directions='''## Step 1 
something here
## Step 2 
something else here
## Step 3
last step''', notes='', author=request.user)
    new1.save()
    new2 = Recipe.objects.create(name='Pancake', description='Pancakes Yay 🥞',
                                prep='0:10:00', cook='0:30:00', servings=5, image='media/download_4.jpeg', ingredients='Sample list of ingredients', 
                                directions='''## Step 1 
something here
## Step 2 
something else here
## Step 3
last step''', notes='', author=request.user)
    new2.save()
    new3 = Recipe.objects.create(name='Sandwich', description='Sandwich to eat while you\'re bored during quarantine 🥪',
                                prep='0:05:00', cook='0:10:00', servings=5, image='media/download_5.jpeg', ingredients='Sample list of ingredients', 
                                directions='''## Step 1 
something here
## Step 2 
something else here
## Step 3
last step''', notes='', author=request.user)
    new3.save()
    new4 = Recipe.objects.create(name='Salad', description='Healthy salad coming your way 🥗',
                                prep='0:15:00', cook='0:20:00', servings=5, image='media/salad_Mz61H85.jpg', ingredients='Sample list of ingredients', 
                                directions='''## Step 1 
something here
## Step 2 
something else here
## Step 3
last step''', notes='', author=request.user)
    new4.save()
    # image_url = 'https://images.media-allrecipes.com/userphotos/1044986.jpg'
    # name, description, prep, cook, servings, image, ingredients, directions, notes, author
    
    return 200