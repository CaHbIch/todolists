from django.db import models

from todolist.core.models import User


class TgUser(models.Model):
    objects = None

    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграм"

    tg_user_id = models.IntegerField(verbose_name="ID пользователя в телеграм")
    tg_chat_id = models.IntegerField(verbose_name="ID чата в телеграм")
    verification_code = models.IntegerField(verbose_name="Код для верификации")
    user = models.ForeignKey(
        User, verbose_name="Пользователь приложения", on_delete=models.PROTECT, null=True
    )
