from django.contrib import admin
from .models import Entry, Tags, UsefulLinks, Videos

admin.site.register(Entry)
admin.site.register(Tags)
admin.site.register(UsefulLinks)
admin.site.register(Videos)

# Register your models here.
