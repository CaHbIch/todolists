from django.db import transaction     # type: ignore

from django_filters.rest_framework import DjangoFilterBackend      # type: ignore
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView     # type: ignore
from rest_framework import permissions, filters     # type: ignore
from rest_framework.pagination import LimitOffsetPagination     # type: ignore

from goals.models import Board, Goal     # type: ignore
from goals.serializers import BoardCreateSerializer, BoardListSerializer, BoardSerializer     # type: ignore
from goals.permissions import BoardPermissions     # type: ignore


class BoardCreateView(CreateAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BoardCreateSerializer


class BoardListView(ListAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated, BoardPermissions]
    serializer_class = BoardListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = ["title"]
    ordering = ["title"]

    def get_queryset(self):
        return Board.objects.filter(
            participants__user=self.request.user, is_deleted=False
        )


class BoardView(RetrieveUpdateDestroyAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated, BoardPermissions]
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(
            participants__user=self.request.user, is_deleted=False
        )

    def perform_destroy(self, instance: Board):
        # При удалении доски помечаем ее как is_deleted,
        # «удаляем» категории, обновляем статус целей
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.categories.update(is_deleted=True)
            Goal.objects.filter(category__board=instance).update(
                status=Goal.Status.archived
            )
        return instance


