from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    return render(request, 'base.html')


def search(request):
    todo_items = Todo.objects.all().order_by("-added_date")

    return render(request, 'todo/index.html', {
        "todo_items" : todo_items
    })


def add_todo(request):
    current_date = timezone.now()
    current_text = request.POST["content"]
    Todo.objects.create(added_date=current_date, text=current_text)
    return HttpResponseRedirect("/search")


def delete_todo(request, todo_id):
    # print(todo_id)
    
    return HttpResponseRedirect("/search")
