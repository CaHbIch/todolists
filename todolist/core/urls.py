from django.urls import path     # type: ignore
from .views import *     # type: ignore

urlpatterns = [
    path('signup', SignUpView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', UserRetrieveUpdateView.as_view()),
    path('update_password', PasswordUpdateView.as_view())
]
