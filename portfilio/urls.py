from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    # path('about/', views.about, name='about'),
    # path('skills/', views.skills, name='skills'),
    # path('projects/', views.projects, name='projects'),
    path('portifilio/index.html', views.contact, name='contact')

]
