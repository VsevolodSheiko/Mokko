from rest_framework import throttling
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
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]



class VisitorViewSet(ModelViewSet):
    queryset = Visitor.objects.all().order_by("id")
    serializer_class = VisitorSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = VisitorFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IngredientFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]
    


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderItemFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]


class FreeTableViewSet(ModelViewSet):
    queryset = FreeTable.objects.all()
    serializer_class = FreeTableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FreeTableFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]


class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilterSet
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]
