from django.http import HttpResponse
from django.shortcuts import render


def helloworld(request):
    return HttpResponse("Hello, world.")


def taskList(request):
    return render(request, 'tasks/list.html')


def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})