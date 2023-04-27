from django_filters import *

from coffeehouse.models import coffeeshop, category, freetable, ingredient, order, orderitem, product, promotion, review, visitor

class CoffeeShopFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    address = CharFilter(field_name="address", lookup_expr="icontains")
    phone = CharFilter(field_name="phone", lookup_expr="icontains")
    city = CharFilter(field_name="city", lookup_expr="icontains")
    description = CharFilter(field_name="description", lookup_expr="icontains")
    
    class Meta:
        model = coffeeshop.CoffeeShop
        fields = ["id", "address", "phone", "city", "description"]



class VisitorFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")
    email = CharFilter(field_name="email", lookup_expr="icontains")
    password = CharFilter(field_name="password", lookup_expr="icontains")
    date_joined = DateFilter(field_name="date_joined", lookup_expr="exact")

    class Meta:
        model = visitor.Visitor
        fields = ["id", "first_name", "last_name", "email", "password", "date_joined"]


class CategoryFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    name = CharFilter(field_name="name", lookup_expr="icontains")
    description = CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = category.Category
        fields = ["id", "name", "description"]
    

class ProductFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    name = CharFilter(field_name="name", lookup_expr="icontains")
    price = CharFilter(field_name="price", lookup_expr="icontains")
    category = CharFilter(field_name="category", lookup_expr="icontains")
    description = CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = product.Product
        fields = ["id", "name", "price", "category", "description"]


class IngredientFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    name = CharFilter(field_name="name", lookup_expr="icontains")
    unit = CharFilter(field_name="unit", lookup_expr="exact")
    price_per_unit = NumberFilter(field_name="price_per_unit", lookup_expr="exact")

    class Meta:
        model = ingredient.Ingredient
        fields = ["id", "name", "unit", "price_per_unit"]


class OrderFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    date_time = DateFilter(field_name="date_time", lookup_expr="exact")
    coffee_shop = CharFilter(field_name="address", lookup_expr="exact")
    status = CharFilter(field_name="status", lookup_expr="icontains")

    class Meta:
        model = order.Order
        fields = ["id", "date_time", "coffee_shop", "status"]


class OrderItemFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    order = NumberFilter(field_name="id", lookup_expr="exact")
    item = NumberFilter(field_name="id", lookup_expr="exact")
    quantity = NumberFilter(field_name="id", lookup_expr="exact")
    unit_price = NumberFilter(field_name="id", lookup_expr="exact")

    class Meta:
        model = orderitem.OrderItem
        fields = ["id", "order", "item", "quantity", "unit_price"]


class FreeTableFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    seats = NumberFilter(field_name="seats", lookup_expr="exact")
    is_available = BooleanFilter(field_name="is_available", lookup_expr="exact")

    class Meta:
        model = freetable.FreeTable
        fields = ["id", "seats", "is_available"]


class PromotionFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    name = CharFilter(field_name="name", lookup_expr="icontains")
    description = CharFilter(field_name="description", lookup_expr="icontains")
    start_date = DateFilter(field_name="start_date", lookup_expr="exact")
    end_date = DateFilter(field_name="end_date", lookup_expr="exact")
    discount = NumberFilter(field_name="discount", lookup_expr="exact")
    product_type = NumberFilter(field_name="product_type", lookup_expr="exact")

    class Meta:
        model = promotion.Promotion
        fields = ["id", "name", "description", "start_date", "end_date", "discount", "product_type"]


class ReviewFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    product = NumberFilter(field_name="product", lookup_expr="exact")
    visitor = NumberFilter(field_name="visitor", lookup_expr="exact")
    rating = NumberFilter(field_name="rating", lookup_expr="exact")
    context = CharFilter(field_name="context", lookup_expr="icontains")

    class Meta:
        model = review.Review
        fields = ["id", "product", "visitor", "rating", "context"]
        