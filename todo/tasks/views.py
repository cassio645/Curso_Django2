from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .models import Task
from .forms import TaskForm


def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})


def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Fazendo'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/editTask.html',{'form': form, 'task': task})
    else:
        return render(request, 'tasks/editTask.html',{'form': form, 'task': task})


def helloworld(request):
    return HttpResponse("Hello, world.")


def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
