from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-story/', views.create_story, name='create_story'),
    path('story/<pk>/', views.story_view, name='story_view'),
    path('story/<pk>/create-task/', views.create_task, name='create_task'),
    path('story/<pk>/task/<task_pk>/', views.task_view, name='task_view'),
    path('story/<pk>/task/<task_pk>/create-time/', views.create_time, name='create_time'),
    path('add-developer/', views.add_developer, name='add_developer'),
    path('create-sprint/', views.create_sprint, name='create_sprint')
]