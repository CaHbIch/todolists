from rest_framework import serializers     # type: ignore

from .models import TgUser     # type: ignore


class TgUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = "__all__"
        read_only_fields = ("tg_user_id", "tg_chat_id")
