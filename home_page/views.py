from django.shortcuts import render
from django.views.generic import ListView
from .models import HomePagePost


class HomePage(ListView):
    model = HomePagePost
    context_object_name = "posts"
    template_name = "home_page/home_page.html"
    extra_context = {"navbar_home": " active"}
