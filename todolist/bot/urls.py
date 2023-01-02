from django.urls import path     # type: ignore
import bot.views as views     # type: ignore

urlpatterns = [
    path("verify", views.TgUserUpdateView.as_view()),
]