from django.db import models
from datetime import date

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class Author(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Tags(models.Model):
  tag = models.CharField(max_length=50)

  def __str__(self):
    return self.tag

class Entry(models.Model):
  title = models.CharField(max_length=225)
  content = models.TextField()
  pub_date = models.DateField()
  mod_date = models.DateField(default=date.today())
  image = models.CharField(max_length=100)
  author = models.CharField(max_length=100, default="Anonymous")
  tags = models.ManyToManyField(Tags, blank=True)

  def __str__(self):
    return self.title

