
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('input', views.input),
    path('add_question', views.add_question),
    path('data', views.data),
    path('', views.index),
    path('<int:id>', views.detail, name='detail'),
    path('vote/', views.vote, name='vote'),
]
