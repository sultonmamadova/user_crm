from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from users.forms import UserForm

User = get_user_model()
User = get_user_model()

class UserListView(ListView):
    template_name = "users/users_list.html"
    queryset = User.objects.all()

class UserDetailView(DetailView):
    template_name = "users/users_detail.html"
    queryset = User.objects.all()

def users_create(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users-list")

    return render(request, "users/users_update.html", {"form": form})


def users_update(request, pk):
    user = get_object_or_404(User, pk=pk)

    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users-list")

    return render(request, "users/users_update.html", {"form": form})


def users_delete(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        user.delete()
        return redirect("users-list")

    return render(
        request,
        "users/users_delete.html",
        {"object": model_to_dict(user, exclude=["password"])},
    )
    