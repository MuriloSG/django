from django.urls import path
from . import views
urlpatterns = [
    path('helloworld/', views.hello_world),
    path('', views.task_list, name='task-list'),
    path('newtask/', views.new_task, name='new-task'),
    path('task/<int:id>', views.task_view, name='task-view'),
    path('edit/<int:id>', views.edit_task, name='edit-task'),
    path('delete/<int:id>', views.delete_task, name='delete-task'),
]