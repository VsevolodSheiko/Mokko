from rest_framework import serializers
from django.contrib.auth.models import User
from coffeehouse.models import coffeeshop, category, freetable, ingredient, order, orderitem, product, promotion, review, visitor

#  Models Serializers
class CoffeeShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = coffeeshop.CoffeeShop
        fields = ['id', 'address', 'city', 'phone', 'description']


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = visitor.Visitor
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'date_joined']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.Category
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product.Product
        fields = ['id', 'name', 'price', 'category', 'description']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ingredient.Ingredient
        fields = ['id', 'name', 'unit', 'price_per_unit']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order.Order
        fields = ['id', 'date_time', 'coffee_shop', 'status']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderitem.OrderItem
        fields = ['id', 'order', 'item', 'quantity', 'unit_price']


class FreeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = freetable.FreeTable
        fields = ['id', 'seats', 'is_available']


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = promotion.Promotion
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'discount', 'product_type']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review.Review
        fields = ['id', 'product', 'visitor', 'rating', 'context']


#  Custom Serializers
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
    
    def create(self, validated_data):
        customer = User.objects.create_user(**validated_data)
        return customer