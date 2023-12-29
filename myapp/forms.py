from django import forms
from .models import Project

class CreateNewTask(forms.Form ):
    tittle = forms.CharField(label="Titulo de la tara", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description  = forms.CharField(label="Descripcion de la Tarea",widget=forms.Textarea(attrs={'class': 'input'}))
    
    projects_list = list(Project.objects.all())
    projects = []

    for i in projects_list:
        projects.append((i.id, i.name))


    project = forms.ChoiceField(choices=projects, widget=forms.Select(attrs={'class':'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
