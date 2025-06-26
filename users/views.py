from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import LoginUserForm, ChangePasswordUserForm
from .models import Profile


class UserAuth(LoginView):
    form_class = LoginUserForm
    template_name = 'users/auth.html'
    extra_context = {"navbar_user": " active"}

    def get_success_url(self):
        return reverse_lazy('home_page')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


class ChangePasswordUser(PasswordChangeView):
    template_name = 'users/password_change_form.html'
    extra_context = {"navbar_user": " active"}

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'id': self.request.user.id})


def profile_user(request, id):
    profile = Profile.objects.get(id=id)
    return render(request, 'users/profile.html', {'profile': profile, "navbar_user": " active"})


def logout_user(request):
    logout(request)
    return redirect('home_page')
