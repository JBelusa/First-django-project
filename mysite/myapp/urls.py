from django.urls import path
from . import views


urlpatterns = [
    path("home", views.home, name="home"),
    path("users", views.users, name="users"),
    path("users_search", views.search, name="users_search"),
    path("statistics", views.statistics, name="statistics"),
    path("controls", views.createUser, name="controls"),
    path("user/<int:userid>", views.user, name="user"),
    path("user_delete/<int:id>/", views.user_delete, name="user_delete"),
    path("user_update/<int:id>", views.user_update, name="user_update"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("register", views.user_register, name="register"),
]
