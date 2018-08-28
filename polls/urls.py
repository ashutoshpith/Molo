from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
     path('<int:ques_id>/', views.detail, name='detail'),
     path('<int:ques_id>/results/', views.results, name='results'),
     path('about/', views.about, name = 'about'),
     path('contact/', views.contact, name = 'contact')


]
urlpatterns += staticfiles_urlpatterns()