from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework import viewsets

from .api_documentation import payment_schema_view, extend_schema
from .models import Payment
from .serializers import PaymentCreateSerializer, PaymentDetailSerializer


@extend_schema(tags=["Платежи"])
@payment_schema_view()
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    http_method_names = ["get", "post", "delete"]

    def get_serializer_class(self):
        if self.action == "create":
            return PaymentCreateSerializer
        return PaymentDetailSerializer

    @method_decorator(cache_page(60 * 15, key_prefix="payment_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user_id = self.request.user.id
        serializer.save(user_id=user_id)
        cache.delete("payment_list")

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("payment_list")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("payment_list")
