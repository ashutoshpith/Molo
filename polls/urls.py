from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('<int:ques_id>/', views.detail, name='detail'),
     path('<int:ques_id>/results/', views.results, name='results'),

]