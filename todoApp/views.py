from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
# Create your views here.
def homepage(request):
    todos=Todo.objects.all()
    return render(request,'index.html',{'todos':todos})

#Сохранение данных в БД
def create(request):
    if request.method=='POST':
        todo=Todo()
        todo.title=request.POST.get('title')
        todo.description=request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')

#Изменение данных из БД
def edit(request,id):
    try:
        todo=Todo.objects.get(id=id)
        if request.method=='POST':
            todo.title=request.POST.get("title")
            todo.description=request.POST.get("description")
            todo.save()
            return HttpResponseRedirect('/')

        else:
            return render(request,'edit.html',{'todo':todo})

    except Todo.DoesNotExist:
        return HttpResponseNotFound("<h2>Задача не найдана</h2>")

#Удаление данных из БД
def delete(request,id):
    try:
        todo=Todo.objects.get(id=id)
        todo.delete()
        return HttpResponseRedirect('/')
    except Todo.DoesNotExist:
        return HttpResponseNotFound("<h2>Задача не найдена</h2>")