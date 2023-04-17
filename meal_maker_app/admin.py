from django.contrib import admin
from .models import image, tags, ingredients, recipies

admin.site.register(image)
admin.site.register(recipies)
admin.site.register(ingredients)
admin.site.register(tags)
