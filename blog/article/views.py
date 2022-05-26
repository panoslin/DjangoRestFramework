from rest_framework import (
    filters,
    viewsets,
)
from .models import Article
from .serializers import (PaginationSerializer, ArticleListSerializer)
from .filters import ArticleFilter
from rest_framework_filters.backends import RestFrameworkFilterBackend


class ArticleViewSet(viewsets.ModelViewSet):
    model = Article
    serializer_class = ArticleListSerializer
    filter_backends = (
        RestFrameworkFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_class = ArticleFilter
    pagination_class = PaginationSerializer
    search_fields = [
        "title",
        "desc",
        "content",
        "author"
    ]
    ordering_fields = [
        "created_at",
        "title"
    ]
    ordering = [
        "created_at"
    ]
    queryset = Article.objects.all()

    # def create(self, request, *args, **kwargs):
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # def destroy(self, request, *args, **kwargs):
    #     pass
