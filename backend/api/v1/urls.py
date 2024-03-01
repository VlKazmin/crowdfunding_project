from django.urls import path, include

from drf_spectacular.views import SpectacularSwaggerView

from .router_settings import CustomDjoserUserRouter

from users.views import UserViewSet
from collects.views import CollectViewSet
from payments.views import PaymentViewSet


app_name = "api"

# Routers v1
router_v1 = CustomDjoserUserRouter()

# Register
router_v1.register(r"users", UserViewSet, "users")
router_v1.register(r"collects", CollectViewSet, "collects")
router_v1.register(r"payments", PaymentViewSet, basename="payment")


# URL
urlpatterns = [
    path("", include(router_v1.urls)),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger"),
]
