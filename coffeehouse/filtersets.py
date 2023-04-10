from django_filters import FilterSet, CharFilter, NumberFilter

from coffeehouse.models import *

class CoffeeShopFilterSet(FilterSet):
    id = NumberFilter(field_name="id", lookup_expr="exact")
    address = CharFilter(field_name="address", lookup_expr="icontains")
    phone = CharFilter(field_name="phone", lookup_expr="icontains")
    city = CharFilter(field_name="city", lookup_expr="icontains")
    description = CharFilter(field_name="description", lookup_expr="icontains")
    
    class Meta:
        model = CoffeeShop
        fields = ["id", "address", "phone", "city", "description"]



class VisitorFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    date_joined = models.DateField()

    class Meta:
        model = Visitor
        fields = []


class CategoryFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        model = Category
        fields = []
    

class ProductFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    price = models.FloatField(default=0.00, null=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()

    class Meta:
        model = Product
        fields = []


class IngredientFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    price_per_unit = models.FloatField(default=0.00)

    class Meta:
        model = Ingredient
        fields = []


class OrderFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=15)

    class Meta:
        model = Order
        fields = []


class OrderItemFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    unit_price = models.ManyToManyField(to=Product, related_name="products")

    class Meta:
        model = OrderItem
        fields = []


class FreeTableFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    seats = models.IntegerField()
    is_available = models.BooleanField()

    class Meta:
        model = FreeTable
        fields = []


class PromotionFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    discount = models.IntegerField()
    product_type = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        model = Promotion
        fields = []


class ReviewFilterSet(FilterSet):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    visitor = models.ForeignKey(Visitor, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    context = models.TextField()

    class Meta:
        model = Review
        fields = []
        