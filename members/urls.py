from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    #path('', views.members, name='members'),
    path('', views.home, name='home'),
    path('details/<int:id>', views.details, name='details'),
    path('blogIndex', views.blogIndex, name="blog"),
    path('about', views.about, name="about"),
    path('blog/<int:id>', views.blogItem, name="blogItem"),
    path('resources', views.resources, name="resources"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))
]
