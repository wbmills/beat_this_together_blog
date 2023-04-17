from django.db import models
from multiselectfield import MultiSelectField


class image(models.Model):
    image = models.ImageField(upload_to="static/frank-content/", default="image.jpg")
    name = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.name


class tags(models.Model):
    name = models.CharField(max_length=100, help_text='Tags are used to sort ingredients and recipes.')

    def __str__(self):
        return self.name

class ingredients(models.Model):
    name = models.CharField(max_length=100, default="None", help_text='The name of the ingredient')
    cost = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, help_text='The cost in £ - format = [pounds].[pennies] e.g. 4.5')
    tag = models.ManyToManyField(tags, null=True, blank=True, help_text='This can mean you can sort recipies in terms of veggie, vegan, niceness, etc')

    def __str__(self):
        return self.name


class recipies(models.Model):
    choices = ((0, "0"),
               (1, "1"),
               (2, "2"),
               (3, "3"),
               (4, "4"),
               (5, "5"))
    name = models.CharField(max_length=100, default='', blank=True, help_text='Name of the meal')
    timeTakenToMake = models.IntegerField(default=0, help_text='Total time taken to make meal in minutes')
    ingredients = models.ManyToManyField(ingredients, help_text='Select the ingredients in the meal')
    recentWetness = MultiSelectField(choices=choices, max_choices=1, default=0,
                               max_length=100,
                               help_text='Choose just one value')
    instructions = models.TextField(help_text='How to make the meal')
    tag = models.ManyToManyField(tags, null=True, blank=True)
    avgWetness = models.FloatField(default=0.0, help_text="Don't edit this one, it'll change itself")

    def __str__(self):
        return self.name

