from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from myapp.models import Users
from myapp.forms import UsersForm, RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.


def home(request):
    return render(request, "myapp/main.html")


def users(request):
    users = Users.objects.all()
    users_count = users.count()
    return render(
        request, "myapp/users.html", {"users": users, "users_count": users_count}
    )


def statistics(request):
    return render(request, "myapp/statistics.html")


def controls(request):
    return render(request, "myapp/controls.html")


def getUsers(request):
    allusers = list(Users.objects.all().values())
    return JsonResponse(allusers, safe=False)


def getUserById(request):
    usersById = Users.objects.get(id=4).name

    # return JsonResponse(usersById, safe=False)
    return HttpResponse(usersById)


# Search function
def search(request):
    # print(request.GET)
    # query_dict = request.GET
    select = request.GET.get("search-option")

    query = request.GET.get("query")

    searched_category, query = select_option(select, query)

    searched_user = Users.objects.filter(**{searched_category: query})

    context = {
        "users": searched_user,
        "user_not_found": f"User with this {select} has not been found",
        "search_option": f"Users found with searched {select}:",
    }
    # print(context.get("users").values())

    return render(request, "myapp/search.html", context)


def select_option(select, query):
    searched_category = None
    match select:
        case "ID":
            searched_category = "id"
            if not query.isdigit():
                query = None
        case "name":
            searched_category = "name"
        case "surname":
            searched_category = "surname"
        case "personID":
            searched_category = "personid"
        case "Uuid":
            searched_category = "uuid"
    return searched_category, query


def user(request, userid):
    user = Users.objects.get(id=userid)
    return render(request, "myapp/user.html", {"user": user})


def createUser(request):

    if request.method == "POST":
        # print("Creating post user:", request.POST)
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    else:
        form = UsersForm()

    context = {"form": form}
    return render(request, "myapp/controls.html", context)


def user_delete(request, id):
    user = Users.objects.get(id=id)

    if request.method == "POST":
        user.delete()
        return redirect("users")  # Redirect to a page after deletion

    return render(request, "myapp/user_delete.html", {"user": user})


def user_update(request, id):
    user = Users.objects.get(id=id)
    if request.method == "POST":
        form = UsersForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users")
        HttpResponse("User updated successfully")
    else:
        form = UsersForm()
    context = {"form": form}
    return render(request, "myapp/user_update.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Wrong credentials, username or password is incorrect",
                }
            )
    return JsonResponse({"status": "error", "message": "Invalid request"})


def user_register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account successfully created for " + user)
            return redirect("home")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "myapp/register.html", context)


def user_logout(request):
    logout(request)
    return redirect("home")


def user_account(request):
    user = request.user
    user_profile = request.user.profile
    if request.method == "POST":

        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)

        if u_form.is_valid() and p_form.is_valid():
            print(user.first_name + " " + user.last_name)
            print(u_form.is_valid())
            print(p_form.is_valid())
            u_form.save()
            p_form.save()

    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user_profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "myapp/account.html", context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your password has been successfully updated!")
            return redirect("home")
    else:
        form = PasswordChangeForm(user=request.user)
    context = {"form": form}
    return render(request, "myapp/change_password.html", context)
