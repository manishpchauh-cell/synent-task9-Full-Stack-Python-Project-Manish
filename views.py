from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, TaskForm
from .models import Task


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("task_list")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")

    return render(
        request,
        "task_list.html",
        {"tasks": tasks},
    )


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(request, "Task Added Successfully")
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(
        request,
        "task_form.html",
        {"form": form},
    )


@login_required
def edit_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated Successfully")
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "task_form.html",
        {"form": form},
    )


@login_required
def delete_task(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task Deleted Successfully")
        return redirect("task_list")

    return render(
        request,
        "delete.html",
        {"task": task},
    )
    from django.shortcuts import render

def home(request):
    return render(request, "home.html")