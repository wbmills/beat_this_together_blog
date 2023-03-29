from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from random import randint
from .models import Member, Entry, Author
import os


def members(request):
    return HttpResponse("Hello World!")


def blogItem(request, id):
    """
    f = open("static/" + file.title, "r", encoding="utf-8")
    title = f.readline()
    content = ""
    content = f.readlines()[1:]
    f.close()
    """
    
    blog = Entry.objects.get(id=id)
    content = blog.content
    return render(request, "blog.html", context={"blog":blog,
                                                 "content":content})


def blogIndex(request):
    files = []
    blogs = Entry.objects.all().values()
    for file in os.listdir("static"):
        if file.endswith(".txt"):
            files.append(file)
    return render(request, "blogIndex.html", context={"files": blogs})


def about(request):
    return render(request, "about.html", context={})


def hello(request):
    wordList = ["lovely", "beautiful", "funny"]
    rand = randint(0, len(wordList) - 1)
    word = wordList[rand]
    m = Member.objects.all().values()
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Member()
            post.firstname = request.POST.get('fname')
            post.lastname = request.POST.get('lname')
            post.save()
    return render(request, 'names.html', context={"word": word,
                                                  "mymembers": m})  # context must be dict


def details(request, id):
    m = Member.objects.get(id=id)
    c = {"member": m}
    return render(request, "details.html", context=c)
