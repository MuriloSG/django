from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import  Task
# Importando formulario
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def task_list(request):
    search = request.GET.get('search')
    filter_value = request.GET.get('filter')
    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    elif filter_value:
        filter_bool = filter_value == '1'
        print(filter_bool)
        tasks = Task.objects.filter(completed=filter_bool, user=request.user)
        print(tasks)
    else: 
        tasks_list = Task.objects.all().order_by(
            '-created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks})


@login_required
def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'tarefa criada com sucesso!')
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


@login_required
def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if (form.is_valid()):
            task.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada!')
    return redirect('/')

def hello_world(request):
    return HttpResponse("Hello world")
