
from django.contrib import admin
from django.urls import path,include
from . import views
# from project_4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include("first_app.urls")),
    path('', views.home),
]
