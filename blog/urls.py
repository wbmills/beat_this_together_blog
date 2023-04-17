from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    path('mam/', include('meal_maker_app.urls'))
]
