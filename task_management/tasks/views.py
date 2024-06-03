from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            # task_form.cleaned_data['author'] = request.user
            task_form.instance.author = request.user
            task_form.save()
            return redirect('show_task')
    else:
        task_form = forms.TaskForm(request.POST)
    return render(request, 'add_task.html', {'form' : task_form})

# def show_task(request):    
#     return render(request, 'show_task.html')

def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')    
    return render(request, 'add_task.html', {'form' : task_form})


def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('show_task')

def is_complete(request, id):
    task = models.Task.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('show_task')