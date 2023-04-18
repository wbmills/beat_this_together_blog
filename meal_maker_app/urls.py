from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    #path('', views.home, name='home'),
    #path('password', views.pw, name='pw'),
    #path('<str:clicked>/', views.home, name='home'),
    path('frank', views.frankContent, name="frankContent"),
    #path('js-tutorial', views.js_tutorial, name='js_tutorial'),
    #path('create', views.createRecipe, name='create'),
]