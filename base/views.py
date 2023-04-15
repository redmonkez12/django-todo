from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from base.forms import UserForm, TodoForm
from base.models import Todo


# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request, "home.html")


@login_required(login_url='login')
def todos(request):
    todos = Todo.objects.all()
    return render(request, "todos.html", {"todos": todos})


@login_required(login_url='login')
def todo(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, "todo.html", {"todo": todo})


@login_required(login_url='login')
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(
                request, 'The todo has been created successfully.')
            return redirect('todos')

        messages.error(request, 'Please correct the following errors:')

    return render(request, "create_todo.html")


def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.user != todo.user:
        messages.error(request, 'Todo not exists')

    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo has been deleted')

    return redirect("todos")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']

        # print(username, password)
        user = authenticate(request, username=username, password=password)
        # print(user)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, "register.html")


def logout_user(request):
    logout(request)
    return redirect("home")
