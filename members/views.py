from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from random import randint
from .models import Member, Entry, Author, Tags, UsefulLinks, Videos
import os

theme = "bg-light"

def videos(request):
    content = Videos.objects.all()
    c = {"content":content}
    return render(request, 'videos.html', context=c)


def resources(request):
    links = UsefulLinks.objects.all()
    return render(request, 'resources.html', context={'links': links})

def blogItem(request, id):
    """
    f = open("static/" + file.title, "r", encoding="utf-8")
    title = f.readline()
    content = ""
    content = f.readlines()[1:]
    f.close()
    """
    
    blog = Entry.objects.get(id=id)
    content = blog.content.replace("â€™", "'").replace("â€˜", "'").replace("â€œ", '"')
    return render(request, "blog.html", context={"blog":blog,
                                                 "c":content,
                                                 "theme":theme})


def blogIndex(request, filter = "None"):
    if filter != "None":
        t = Tags.objects.get(tag=filter)
        blogs = Entry.objects.all().values().order_by("-pub_date").filter(tags=t)
    else:
        blogs = Entry.objects.all().values().order_by("-pub_date")
    return render(request, "blogIndex.html", context={"files": blogs,
                                                      "theme":theme})


def about(request):
    return render(request, "about.html", context={"theme":theme})


def home(request):
    post = Entry.objects.latest("pub_date")
    content = "Click the link to read more..."

    fpost = Entry.objects.get(title="Coping with Calorie Legislation: How to deal with unhelpful information on menus")
    return render(request, 'home.html', context={"theme":theme,
                                                 "post":post,
                                                 "content":content,
                                                 "fpost":fpost})  # context must be dict


def details(request, id):
    m = Member.objects.get(id=id)
    c = {"member": m,
         "theme":theme}
    return render(request, "details.html", context=c)
