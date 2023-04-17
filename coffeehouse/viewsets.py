from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from coffeehouse.pagination import CustomPagination

from coffeehouse.models.category import Category
from coffeehouse.models.coffeeshop import CoffeeShop
from coffeehouse.models.visitor import Visitor
from coffeehouse.models.product import Product
from coffeehouse.models.ingredient import Ingredient
from coffeehouse.models.order import Order
from coffeehouse.models.orderitem import OrderItem
from coffeehouse.models.freetable import FreeTable
from coffeehouse.models.promotion import Promotion
from coffeehouse.models.review import Review


from coffeehouse.serializers import *
from coffeehouse.filtersets import *

class CoffeeShopViewSet(ModelViewSet):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CoffeeShopFilterSet


class VisitorViewSet(ModelViewSet):
    queryset = Visitor.objects.all().order_by("id")
    serializer_class = VisitorSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = VisitorFilterSet


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilterSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilterSet


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IngredientFilterSet


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilterSet


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderItemFilterSet


class FreeTableViewSet(ModelViewSet):
    queryset = FreeTable.objects.all()
    serializer_class = FreeTableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FreeTableFilterSet


class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilterSet


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilterSet
