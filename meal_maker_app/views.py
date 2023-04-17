from django.shortcuts import render, get_object_or_404
import os
from blog import settings as s
from .models import image, tags, ingredients, recipies

def home(request, clicked=None):
    r = []
    allMealTags = tags.objects.all()
    n = recipies.objects.all().count()
    if clicked:
        info = recipies.objects.get(id=clicked)
        ix = info.ingredients.all()
        list = ix.values()
        totalCost = 0
        for i in ix:
            totalCost += i.cost
    else:
        info = None
        list = None
        totalCost = 0
    for recipe in recipies.objects.all():
        r.append(recipe)
    c = {'recipeList': r,
         'clicked': clicked,
         'info': info,
         'list': list,
         'cost':totalCost,
         'tags':allMealTags,
         'numRecipes': n}
    return render(request, 'homeMeal.html', context=c)


def createRecipe(request):
    c = {}
    return render(request, 'create.html', context=c)


def js_tutorial(request):
    c = {}
    return render(request, 'tutorial.html', context=c)


def frankContent(request):
    files = image.objects.all()
    c = {"files": files}
    return render(request, "franks-page.html", context=c)

def pw(request):
    return render(request, 'password.html', context={})