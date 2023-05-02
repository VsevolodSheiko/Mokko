from rest_framework import serializers
from django.contrib.auth.models import User
from coffeehouse.models import coffeeshop, category, freetable, ingredient, order, orderitem, product, promotion, review, visitor

#  Models Serializers
class CoffeeShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = coffeeshop.CoffeeShop
        fields = '__all__'


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = visitor.Visitor
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product.Product
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ingredient.Ingredient
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order.Order
        fields = ['id', 'date_time', 'table', 'status']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderitem.OrderItem
        fields = '__all__'


class FreeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = freetable.FreeTable
        fields = '__all__'


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = promotion.Promotion
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review.Review
        fields = '__all__'


#  Custom Serializers
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        customer = User.objects.create_user(**validated_data)
        return customer