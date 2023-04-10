from django.contrib import admin
from .models import Entry, Tags, UsefulLinks

admin.site.register(Entry)
admin.site.register(Tags)
admin.site.register(UsefulLinks)

# Register your models here.
