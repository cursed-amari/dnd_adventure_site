from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CreateAdventure, ChangeAdventure
from .models import Adventure
from .utils import *

from django.shortcuts import render, get_object_or_404


class AdventurePage(ListView):
    model = Adventure
    context_object_name = "adventures"
    template_name = "adventure/adventure_page.html"
    extra_context = {"navbar_adventure": " active"}
    ordering = ["-time_update"]


def adventure_detail(request, slug):
    post = get_object_or_404(Adventure, slug=slug)
    print(post.file.url)
    context = {
        "image": post.image.url,
        "title": post.title,
        "slug": post.slug,
        "username": post.user.username,
        "duration": post.duration,
        "amount_players": post.amount_players,
        "level": post.level,
        "description": post.description,
        "file": post.file.url,
        "time_update": post.time_update,
        "navbar_adventure": " active"
    }
    return render(request, "adventure/adventure_detail.html", context)


class UpdateAdventure(UpdateView):
    model = Adventure
    form_class = ChangeAdventure
    template_name = 'adventure/adventure_update.html'
    context_object_name = "adventure"

    def get_success_url(self):
        return reverse_lazy('adventure')


class AdventureCreate(LoginRequiredMixin, CreateView):
    model = Adventure
    form_class = CreateAdventure
    template_name = "adventure/adventure_create.html"
    login_url = reverse_lazy('adventure')

    def form_valid(self, form):
        form.save(commit=False)
        slug = slugify(translation_text_for_slug(form.cleaned_data['title']))
        form.instance.slug = slug
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('adventure')


def user_list_adventure(request):
    posts = Adventure.objects.filter(user=request.user)
    context = {"posts": posts,
               "navbar_adventure": " active"}
    return render(request, "adventure/user_adventures.html", context)

