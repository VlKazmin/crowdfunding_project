from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from djoser.views import UserViewSet as DjoserUserViewSet

from rest_framework.pagination import PageNumberPagination

from .api_documentation import (
    user_schema_view,
    extend_schema,
)

from .models import CustomUser
from .serializers import UserSerializer


@extend_schema(tags=["Пользователи"])
@user_schema_view()
class UserViewSet(DjoserUserViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60 * 15, key_prefix="user_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
        cache.delete("user_list")

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("user_list")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("user_list")
