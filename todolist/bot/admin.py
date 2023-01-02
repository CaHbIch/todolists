from django.contrib import admin      # type: ignore

from bot.models import TgUser     # type: ignore


class BotAdmin(admin.ModelAdmin):
    list_display = ("tg_user_id", "tg_chat_id", "user")
    search_fields = ("tg_user_id", "tg_chat_id", "user")

admin.site.register(TgUser,BotAdmin)
