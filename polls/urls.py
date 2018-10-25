
from django.contrib import admin
from django.urls import path
from . import views
# / 붙이면 현재나의 경로는 vote까지, 없으면 그 전까지 현재경로 , /가 어디서 마무리 됐는가가 경로가 된다.
#  "/" : 상대 경로에서 현재 나의 경로의 기준 이 됨
urlpatterns = [
    path('result/<int:id>', views.result),
    path('input', views.input),
    path('add_question', views.add_question),
    path('<int:number>/data/<str:email>', views.data),
    path('', views.index),
    path('<int:id>', views.detail, name='detail'),
    path('vote/', views.vote, name='vote'),
]
