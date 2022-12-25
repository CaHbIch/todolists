from django.db import models

from .dates_mixin import DatesModelMixin


class Board(DatesModelMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.categories = None

    objects = None

    class Meta:
        verbose_name = "Доска"
        verbose_name_plural = "Доски"

    title = models.CharField(verbose_name="Название", max_length=255)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)