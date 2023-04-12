"""Mokko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from coffeehouse.viewsets import *

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Mokko API Swagger Documentation",
        default_version='v1',
        description="Mokko API Swagger Documentation was created by Vsevolod Sheiko - student of Hillel Python Pro course ",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[],
)

router_model_dict = {
    'coffeeshop': CoffeeShopViewSet,
    'visitor': VisitorViewSet,
    'category': CategoryViewSet,
    'product': ProductViewSet,
    'ingredient': IngredientViewSet,
    'order': OrderViewSet,
    'orderitem': OrderItemViewSet,
    'freetable': FreeTableViewSet,
    'promotion': PromotionViewSet,
    'review': ReviewViewSet
}

for k, v in router_model_dict.items():
    router.register(k, v)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]