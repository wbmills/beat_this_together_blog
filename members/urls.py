from django.urls import path
from . import views

urlpatterns = [
    #path('', views.members, name='members'),
    path('', views.hello, name='hello'),
    path('details/<int:id>', views.details, name='details'),
    path('blogIndex', views.blogIndex, name="blog"),
    path('about', views.about, name="about"),
    path('blog/<int:id>', views.blogItem, name="blogItem")
]