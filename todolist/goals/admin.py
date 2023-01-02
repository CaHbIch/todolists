from typing import Tuple

from django.contrib import admin  # type: ignore

from goals.models import Category, Goal, Comment, Board  # type: ignore


class BaseAdmin(admin.ModelAdmin):
    list_display: Tuple = ("title", "user", "created", "updated")
    search_fields: Tuple = ("title", "user")
    readonly_fields: Tuple = ("created", "updated")


class CategoryAdmin(BaseAdmin):
    pass


class GoalAdmin(BaseAdmin):
    list_display = ("title", "user", "category", "created", "updated")
    search_fields = ("title", "user", "category")


class CommentAdmin(BaseAdmin):
    list_display = ("goal", "user", "created", "updated")
    search_fields = ("goal", "user", "text")


class BoardAdmin(BaseAdmin):
    list_display = ("title", "created", "updated")
    search_fields = ("title",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Board, BoardAdmin)
