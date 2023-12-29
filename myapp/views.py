from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render


from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Ejemplo de Pasar una variable al html'
    return render(request, "index.html", 
                        {
                            'variable': title
                        }
                  )

def hello(request, userName):
    return HttpResponse("Hello world %s" % userName)

def about(request):
    return render(request, 'about.html') 

#Vistas para proyectos
def projects(request):
        projectsList = list(Project.objects.values())


        return render(request, "projects/project.html", {'projects':projectsList}) 

def createProject(request):
     if request.method == 'GET':
        return render(request, 'projects/createProject.html', {
             'form': CreateNewProject()
             })
     
     else:
        print(request.POST['name'])
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
     
def projectDetails(request, id):
     nameProject = Project.objects.get(id=id)
     tasksOfProject = Task.objects.filter(project_id=id)
     #print(tasksOfProject)

     return render(request, "projects/projectDetails.html",{
          'projectName': nameProject,
          'tasks' : tasksOfProject
     })
     

#Vistas para tareas
def tasks(request):
        taskList = Task.objects.all()

        
        return render(request, "tasks/task.html", {'taskList': taskList})

def createTasks(request):
    if request.method == 'GET':
        return render(request, 'tasks/createTask.html', {
                'form': CreateNewTask()
        })
    else:
        #print(request.POST['project'])
        Task.objects.create(tittle=request.POST['tittle'], description= request.POST['description'], project_id = request.POST['project'])
        return redirect('/tasks/')
