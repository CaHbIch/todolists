# Generated by Django 4.0.1 on 2022-12-25 17:12
from typing import Any

from django.db import migrations, models      # type: ignore


class Migration(migrations.Migration):

    initial = True

    dependencies: Any = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_user_id', models.IntegerField(verbose_name='ID пользователя в телеграм')),
                ('tg_chat_id', models.IntegerField(verbose_name='ID чата в телеграм')),
                ('verification_code', models.IntegerField(verbose_name='Код для верификации')),
            ],
            options={
                'verbose_name': 'Пользователь телеграм',
                'verbose_name_plural': 'Пользователи телеграм',
            },
        ),
    ]
