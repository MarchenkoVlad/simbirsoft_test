from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
    path('', views.home, name='start'),
    path('save_answer/', views.save_answer, name='save_answer'),
    path('report/', views.report, name='report'),
]