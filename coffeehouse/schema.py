from graphene_django import DjangoObjectType

from coffeehouse.models import coffeeshop, category, freetable, ingredient, order, orderitem, product, promotion, review, visitor


class CoffeeShopType(DjangoObjectType):
    class Meta:
        model = coffeeshop.CoffeeShop
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = category.Category
        fields = "__all__"


class FreeTableType(DjangoObjectType):
    class Meta:
        model = freetable.FreeTable
        fields = "__all__"


class IngredientType(DjangoObjectType):
    class Meta:
        model = ingredient.Ingredient
        fields = "__all__"


class OrderType(DjangoObjectType):
    class Meta:
        model = order.Order
        fields = "__all__"


class OrderItemType(DjangoObjectType):
    class Meta:
        model = orderitem.OrderItem
        fields = "__all__"


class ProductType(DjangoObjectType):
    class Meta:
        model = product.Product
        fields = "__all__"


class PromotionType(DjangoObjectType):
    class Meta:
        model = promotion.Promotion
        fields = "__all__"


class ReviewType(DjangoObjectType):
    class Meta:
        model = review.Review
        fields = "__all__"


class VisitorType(DjangoObjectType):
    class Meta:
        model = visitor.Visitor
        fields = "__all__"


