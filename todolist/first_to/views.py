from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.views import View
from .models import Todo

# Create your views here.

def index(request):
    todo_user=Todo.objects.all()
    context={
        'todos':todo_user,
    }
    return render(request,'todo_user.html',context)

def task(request,todo_task):
    todo_user=get_object_or_404(Todo,task=todo_task)
    todo_user.mark_as_done()
    return HttpResponse()
    return render(request,'todo_task.index',context,{
        "task":task
    })

def index(request):
    if request.method=="POST":
        Userforms=forms(request.POST)
    if Userforms.is_valid():
        task.append(task)
        return render(request,"Todolist/index.html",{
            "task":task,
            "form":forms
        })