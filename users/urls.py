from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include

from .views import *

urlpatterns = [
    path('login/', UserAuth.as_view(), name="login"),
    path('profile/<int:id>', profile_user, name="profile"),
    path('registration/', register_user, name="register"),
    path('logout/', logout_user, name="logout"),
    path('change-password/', ChangePasswordUser.as_view(), name='password_change'),
]
