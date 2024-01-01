

from django.urls import path
from . import views
# from project_4 import views

urlpatterns = [
    
    path('', views.home,name='home'),
    # path('about/page/<int:id>/', views.about,name='about'),
    path('about/', views.about,name='about'),
]
