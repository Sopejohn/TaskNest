from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Task

# Create your views here.
@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('completed','due_date')
    tasks_count = tasks.count()
    context = {
        'tasks' : tasks,
        'tasks_count' : tasks_count,
    }
    return render(request, 'tasks/tasks.html', context)

@login_required
def create(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            if not task.due_date:
                from django.utils import timezone
                task.due_date = timezone.now()
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('tasks')
        
        else:
            form = TaskForm()

    context = {'form': form}
    return render(request, 'tasks/create.html', context)

@login_required
def edit(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks')

    context = {'form': form}
    return render(request, 'tasks/edit.html', context)

@login_required
def delete(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == "POST":
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('tasks')

    context ={'task': task}
    return render(request, 'tasks/delete.html', context)

@login_required
def toggle(request, pk):
    if request.method != "POST":
        return redirect("tasks")

    task = get_object_or_404(Task, id=pk, user=request.user)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    status = "completed" if task.completed else "marked as pending"
    messages.success(request, f'Task {status}!')
    return redirect("tasks")

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
    