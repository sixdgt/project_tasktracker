from django.shortcuts import render
from .forms import TaskCreateForm

from .models import Task

# Create your views here.
def task_create(request):
    if request.method == "post":
        task = Task()
        task.task_title = request.POST.get('task_title')
        task.task_desc = request.POST.get('task_desc')
        task.task_category = request.POST.get('task_category')
        task.task_assign_date = request.POST.get('task_assign_date')
        task.task_assign_to = request.POST.get('task_assign_to')
        task.task_assigned_by = request.POST.get('task_assigned_by')
        task.task_end_date = request.POST.get('task_end_date')
        task.save()

        template = 'tasks/index.html'
        return render(request, template)
    else:
        create_form = TaskCreateForm()
        template = "tasks/create.html"
        context = {
            "title":"Task Create",
            "body_title": "ToDO App | TASK CREATE",
            "form": create_form
        }
        return render(request, template, context)