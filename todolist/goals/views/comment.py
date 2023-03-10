from django_filters.rest_framework import DjangoFilterBackend     # type: ignore
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView     # type: ignore
from rest_framework import permissions, filters     # type: ignore
from rest_framework.pagination import LimitOffsetPagination     # type: ignore

from goals.models import Comment     # type: ignore
from goals.serializers import CommentCreateSerializer, CommentSerializer     # type: ignore
from goals.permissions import CommentPermissions     # type: ignore


class CommentCreateView(CreateAPIView):
    model = Comment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentCreateSerializer


class CommentListView(ListAPIView):
    model = Comment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = ["created"]
    ordering = ["-created"]
    filterset_fields = ["goal"]

    def get_queryset(self):
        return Comment.objects.filter(
            goal__category__board__participants__user=self.request.user,
        )


class CommentView(RetrieveUpdateDestroyAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [CommentPermissions]

    def get_queryset(self):
        return Comment.objects.filter(
            goal__category__board__participants__user=self.request.user,
        )
