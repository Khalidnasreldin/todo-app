from django.shortcuts import render, redirect
from . models import Task
from . forms import TaskForm
# Create your views here.
def index_view(request):
    form = TaskForm()
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'tasks':tasks, 'TaskForm':form}
    return render(request, 'todo/index.html', context=context)

def update_task_view(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'TaskForm':form}
    return render(request, 'todo/update-task.html', context=context)

def delete_task_view(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    context = {'task':task}
    return render(request, 'todo/delete-task.html', context=context)