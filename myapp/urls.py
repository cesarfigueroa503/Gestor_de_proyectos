from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name="index"), 
    path('about/', views.about, name= "about"),
    path('hello/<str:userName>', views.hello),
    
    path('projects/', views.projects, name="projects"),
    path('projects/createProject', views.createProject, name="createProject"),
    path('projects/details/<int:id>', views.projectDetails, name="projectDetails"),

    path('tasks/', views.tasks, name="tasks"),
    path('tasks/createTask', views.createTasks, name="createTask"),
    

]