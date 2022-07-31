from django.shortcuts import render
from .forms import TaskCreateForm

from .models import Task
from django.core.mail import send_mail

# Create your views here.
def task_index(request):
    tasks = Task.objects.all() # returns whole list of data in dict
    context = {
        "title": "Task Create",
        "body_title": "Task Create | TASK TRACKER",
        "tasks": tasks
    }
    template = "tasks/index.html"
    return render(request, template, context)

def task_update(request):
    if request.method == "POST":
        task = Task.objects.get(id=request.POST.get('id'))
        task.task_title = request.POST.get('task_title')
        task.task_desc = request.POST.get('task_desc')
        task.task_category = request.POST.get('task_category')
        task.task_assign_date = request.POST.get('task_assign_date')
        task.task_assign_to = request.POST.get('task_assign_to')
        task.task_assigned_by = request.POST.get('task_assigned_by')
        task.task_end_date = request.POST.get('task_end_date')
        task.save()

        tasks = Task.objects.all() # returns whole list of data in dict
        context = {
            "title": "Task Index",
            "body_title": "Task Index | TASK TRACKER",
            "tasks": tasks
        }
        template = 'tasks/index.html'
        return render(request, template, context)
    else:
        tasks = Task.objects.all() # returns whole list of data in dict
        context = {
            "title": "Task Index",
            "body_title": "Task List | TASK TRACKER",
            "tasks": tasks
        }
        template = 'tasks/index.html'
        return render(request, template, context)

def task_edit(request, id):
    task = Task.objects.get(id=id)
    context = {
        "title": "Task Edit",
        "body_title": "Task Edit | TASK TRACKER",
        "task": task
    }
    template = "tasks/edit.html"
    return render(request, template, context)

def task_show(request, id):
    task = Task.objects.get(id=id)
    context = {
        "title": "Task Edit",
        "body_title": "Task Show | TASK SHOW",
        "task": task
    }
    template = "tasks/show.html"

    return render(request, template, context)

def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete() # delete data from table

    tasks = Task.objects.all() # returns whole list of data in dict
    context = {
        "title": "Task Create",
        "body_title": "Task Create | TASK TRACKER",
        "tasks": tasks
    }
    template = "tasks/index.html"

    return render(request, template, context)

def task_create(request):
    if request.method == "POST":
        task = Task()
        task.task_title = request.POST.get('task_title')
        task.task_desc = request.POST.get('task_desc')
        task.task_category = request.POST.get('task_category')
        task.task_assign_date = request.POST.get('task_assign_date')
        task.task_assign_to = request.POST.get('task_assign_to')
        task.task_assigned_by = request.POST.get('task_assigned_by')
        task.task_end_date = request.POST.get('task_end_date')
        task.save()

        send_mail(
            'Task Assignment:-' + task.task_title,
            'You are assigned to a task. Task Assign date:- ' + str(task.task_assign_date),
            'c4crypt@gmail.com',
            [task.task_assign_to]
        )
        
        tasks = Task.objects.all() # returns whole list of data in dict
        context = {
            "title": "Task Index",
            "body_title": "Task List | TASK TRACKER",
            "tasks": tasks
        }
        template = 'tasks/index.html'
        return render(request, template, context)
    else:
        create_form = TaskCreateForm()
        template = "tasks/create.html"
        context = {
            "title":"Task Create",
            "body_title": "ToDO App | TASK CREATE",
            "form": create_form
        }
        return render(request, template, context)