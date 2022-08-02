from datetime import datetime
from django.db import models

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=200)
    task_category = models.CharField(max_length=100)
    task_assign_date = models.DateField(null=True, blank=True)
    task_end_date = models.DateField(null=True, blank=True)
    task_assign_to = models.EmailField(default=None, unique=True)
    task_assigned_by = models.CharField(max_length=200)
    task_file = models.FileField()
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_task'
