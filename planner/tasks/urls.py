from django.contrib import admin
from django.urls import path, include
from tasks import views as views

urlpatterns = [
    path('tasks', views.tasks, name='tasks'),
    path('create', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path("toggle/<int:pk>", views.toggle, name="toggle"),
]
