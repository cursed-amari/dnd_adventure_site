from django.urls import path, include
from .views import *

urlpatterns = [
    path('', AdventurePage.as_view(), name="adventure"),
    path('adventure-detail/<slug:slug>/', adventure_detail, name="adventure_detail"),
    path('user-adventure/', user_list_adventure, name="user-adventure"),
    path('create-adventure/', AdventureCreate.as_view(), name="create-adventure"),
    path('update-adventure/<slug:slug>', UpdateAdventure.as_view(), name="update-adventure"),
]
