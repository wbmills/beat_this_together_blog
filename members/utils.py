from django.conf import settings

from members.models import Entry, Author
from datetime import date



def importBlogFromTxtFile(fileName, author="Anonymous", imageFileName="Logo.png"):
    f = open("/static/" + fileName, "r")
    title = f.readline()
    content = f.readlines[1:]
    pub_date = date.today()

    a = Author.objects.create(name=author)
    e = Entry.objects.create(title=title, content=content, pub_date=pub_date,
                             image=imageFileName, author=a)
    a.save()
    e.save()

#importBlogFromTxtFile("blog1.txt", author="Will Mills", imageFileName="/images/menu_icon.png")

f = open("static/blog1.txt", "r")
title = f.readline()
content = f.readlines()[1:]
pub_date = date.today()

a = Author.objects.create(name="Will Mills")
e = Entry.objects.create(title=title, content=content, pub_date=pub_date,
                         image="/images/menu_icon.png", author="Will Mills")
a.save()
e.save()