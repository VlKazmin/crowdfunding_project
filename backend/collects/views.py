from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .api_documentation import collect_schema_view, extend_schema
from .models import Collect
from .serializers import CollectSerializer, CollectCreateSerializer
from .permissions import IsAuthorOrReadOnly


@extend_schema(tags=["Пожертвования"])
@collect_schema_view()
class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action in ["update", "partial_update", "create"]:
            return CollectCreateSerializer
        return CollectSerializer

    @method_decorator(cache_page(60 * 15, key_prefix="collect_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
        cache.delete("collect_list")

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("collect_list")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("collect_list")
