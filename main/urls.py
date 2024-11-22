from django.urls import path
from . import views

urlpatterns = [
    path('', views.createQuestionView, name='question_url'),
    path('success/', views.successView, name='success_url'),
    path('list/', views.listView, name='list_url')
]
