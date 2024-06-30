from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})


def show_tasks(request):
    tasks = TaskModel.objects.all()

    return render(request, 'task_list.html', {"tasks": tasks})

def edit_task(request, id):
    task = TaskModel.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/add_task.html', {'form': form})

def delete_task(request, id):
    task = TaskModel.objects.get(id=id)
    task.delete()
    return redirect('show_tasks')

def complete_task(request, id):
    task = TaskModel.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')