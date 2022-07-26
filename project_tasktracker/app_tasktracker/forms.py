from django import forms
from .models import Task

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_title', 'task_desc','task_category','task_assign_date','task_end_date',\
            'task_assign_to','task_assigned_by')