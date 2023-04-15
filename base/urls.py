from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos", views.todos, name="todos"),
    path("todos/<str:pk>", views.todo, name="todo"),
    path("todo/create", views.create_todo, name="create_todo"),
    path("todo/<str:pk>/delete", views.delete_todo, name="delete_todo"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_user, name="logout"),
]
