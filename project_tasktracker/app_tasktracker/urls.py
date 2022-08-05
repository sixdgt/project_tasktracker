import imp
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tasks/', views.task_index, name='task.list'),
    path('task/create/', views.task_create, name='task.create'),
    path('task/update/', views.task_update, name='task.update'),
    path('task/edit/<int:id>', views.task_edit, name='task.edit'),
    path('task/show/<int:id>', views.task_show, name='task.show'),
    path('task/delete/<int:id>', views.task_delete, name='task.delete'),
    path('user/login/', views.user_login, name='user.login'),
    path('user/logout/', views.user_logout, name='user.logout'),
    path('user/register/', views.user_register, name='user.register'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
