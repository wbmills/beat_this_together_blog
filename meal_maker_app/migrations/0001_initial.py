# Generated by Django 4.1.7 on 2023-04-14 20:29

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='image.jpg', upload_to='static/frank-content/')),
                ('name', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', help_text='The name of the ingredient', max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, help_text='The cost in £ - format = [pounds].[pennies] e.g. 4.5', max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Tags are used to sort ingredients and recipes.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='recipies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='Name of the meal', max_length=100)),
                ('timeTakenToMake', models.IntegerField(default=0, help_text='Total time taken to make meal in minutes')),
                ('recentWetness', multiselectfield.db.fields.MultiSelectField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, help_text='Choose just one value', max_length=100)),
                ('instructions', models.TextField(help_text='How to make the meal')),
                ('avgWetness', models.FloatField(default=0.0, help_text="Don't edit this one, it'll change itself")),
                ('ingredients', models.ManyToManyField(help_text='Select the ingredients in the meal', to='meal_maker_app.ingredients')),
                ('tag', models.ManyToManyField(blank=True, null=True, to='meal_maker_app.tags')),
            ],
        ),
        migrations.AddField(
            model_name='ingredients',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='This can mean you can sort recipies in terms of veggie, vegan, niceness, etc', null=True, to='meal_maker_app.tags'),
        ),
    ]
