from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ecommerce.apps.catalogue.urls", namespace="catalogue")),
    path("checkout/", include("ecommerce.apps.checkout.urls", namespace="checkout")),
    path("basket/", include("ecommerce.apps.basket.urls", namespace="basket")),
    path("account/", include("ecommerce.apps.account.urls", namespace="account")),
    path("orders/", include("ecommerce.apps.orders.urls", namespace="orders")),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
