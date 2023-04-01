from django.conf import settings

from members.models import Entry, Author
from datetime import date

def filetostr(file):
    x = open(f"static/{file}","r", encoding="utf-8")
    r = x.read()

    import datetime
    d = datetime.date.today()

    i = "/images/Logo.jpg"
    return r, d, i
