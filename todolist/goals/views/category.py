from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView     # type: ignore
from rest_framework import permissions, filters     # type: ignore
from rest_framework.pagination import LimitOffsetPagination     # type: ignore
from django_filters.rest_framework import DjangoFilterBackend     # type: ignore

from goals.models import Category, Goal     # type: ignore
from goals.serializers import CategoryCreateSerializer, CategorySerializer     # type: ignore
from goals.permissions import CategoryPermissions     # type: ignore


class CategoryCreateView(CreateAPIView):
    model = Category
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategoryCreateSerializer


class CategoryListView(ListAPIView):
    model = Category
    permission_classes = [CategoryPermissions]
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]
    filterset_fields = ["board", "user"]

    def get_queryset(self):
        return Category.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )


class CategoryView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermissions]

    def get_queryset(self):
        return Category.objects.filter(
            board__participants__user=self.request.user, is_deleted=False
        )

    def perform_destroy(self, instance):
        instance.is_deleted = True

        goals = Goal.objects.filter(category=instance)
        for goal in goals:
            goal.is_deleted = True
            goal.save()

        instance.save()
        return instance
