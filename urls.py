from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Task
from .forms import RegisterForm, TaskForm

# 1. Home Page View
def home(request):
    return render(request, 'home.html')

# 2. Register View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Register hote hi direct login kar dena
            return redirect('task_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# 3. Dashboard / Task List View (Protected)
@login_required(login_url='login')
def task_list(request):
    # Sirf login user ke tasks dikhana
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

# 4. Add Task View (Protected)
@login_required(login_url='login')
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user # Task ko logged-in user se link karna
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

# 5. Edit Task View (Protected)
@login_required(login_url='login')
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

# 6. Delete Task View (Protected)
@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'delete.html', {'task': task})
urlpatterns = [
    path("", views.home, name="home"),

    path("register/", views.register, name="register"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="home"),
        name="logout",
    ),

    path(
        "tasks/",
        views.task_list,
        name="task_list",
    ),

    path(
        "task/add/",
        views.add_task,
        name="add_task",
    ),

    path(
        "task/edit/<int:pk>/",
        views.edit_task,
        name="edit_task",
    ),

    path(
        "task/delete/<int:pk>/",
        views.delete_task,
        name="delete_task",
    ),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('tasks.urls')),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')), # Sabhi app URLs ko include karega
]