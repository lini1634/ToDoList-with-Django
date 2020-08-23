from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
import time


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request,"my_to_do_app/index.html",content)

def createTodo(request):
    user=request.POST['todoContent']
    t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    user_t = user+"\n ("+t + ")"
    new=Todo(content=user_t)
    new.save()
    return HttpResponseRedirect(reverse('index'))

def doneTodo(request):
    done_todo_id=request.GET['todoNum']
    print("완료한 todo의 id",done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
