from django.shortcuts import render, redirect

from .forms import TaskForm
from . models import Task
from django . http import HttpResponse
# Create your views here.

def index(request):
    task_detail = Task.objects.all()
    if request.method=='POST':
        task_name=request.POST.get('task_name')
        task_priority=request.POST.get('task_priority')
        task_date=request.POST.get('task_date')
        task=Task(task_name=task_name,task_priority=task_priority,task_date=task_date)
        task.save()
    return render(request,"index.html",{'task_detail':task_detail})

def delete_task(request,task_id):
    if request.method=='POST':
        task=Task.objects.get(id=task_id)
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

def update_task(request,task_id):
    task=Task.objects.get(id=task_id)
    form=TaskForm(request.POST or None,request.FILES,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'task':task})




