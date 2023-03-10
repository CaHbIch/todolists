from django_filters.rest_framework import DjangoFilterBackend     # type: ignore
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView     # type: ignore
from rest_framework import permissions, filters     # type: ignore
from rest_framework.pagination import LimitOffsetPagination     # type: ignore

from goals.models import Goal     # type: ignore
from goals.serializers import GoalCreateSerializer, GoalSerializer     # type: ignore
from goals.filters import GoalDateFilter     # type: ignore
from goals.permissions import GoalPermissions     # type: ignore


class GoalCreateView(CreateAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCreateSerializer


class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title", "created", "priority", "due_date"]
    ordering = ["-priority", "due_date", "title"]
    filterset_class = GoalDateFilter
    search_fields = ["title", "description"]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user).exclude(status=Goal.Status.archived)


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [GoalPermissions]

    def get_queryset(self):
        return Goal.objects.filter(
            category__board__participants__user=self.request.user,
            is_deleted=False
        )

    def perform_destroy(self, instance):
        instance.status = Goal.Status.archived
        instance.save()
        return instance
