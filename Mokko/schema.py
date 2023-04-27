import graphene
from coffeehouse.schema import *
from coffeehouse.models import coffeeshop, category, freetable, ingredient, order, orderitem, product, promotion, review, visitor


class Query(graphene.ObjectType):
    coffeeshop = graphene.Field(CoffeeShopType, id=graphene.ID(required=True))
    category = graphene.Field(CategoryType, id=graphene.ID(required=True))
    freetable = graphene.Field(FreeTableType, id=graphene.ID(required=True))
    ingredient = graphene.Field(IngredientType, id=graphene.ID(required=True))
    order = graphene.Field(OrderType, id=graphene.ID(required=True))
    orderitem = graphene.Field(OrderItemType, id=graphene.ID(required=True))
    product = graphene.Field(ProductType, id=graphene.ID(required=True))
    promotion = graphene.Field(PromotionType, id=graphene.ID(required=True))
    review = graphene.Field(ReviewType, id=graphene.ID(required=True))
    visitor = graphene.Field(VisitorType, id=graphene.ID(required=True))
    

    def resolve_coffeeshop(self, info, id):
        return coffeeshop.CoffeeShop.objects.get(id=id)
    
    def resolve_category(self, info, id):
        return category.Category.objects.get(id=id)
    
    def resolve_freetable(self, info, id):
        return freetable.FreeTable.objects.get(id=id)
    
    def resolve_ingredient(self, info, id):
        return ingredient.Ingredient.objects.get(id=id)
    
    def resolve_order(self, info, id):
        return order.Order.objects.get(id=id)
    
    def resolve_orderitem(self, info, id):
        return orderitem.Order.objects.get(id=id)
    
    def resolve_product(self, info, id):
        return product.Product.objects.get(id=id)
    
    def resolve_promotion(self, info, id):
        return promotion.Promotion.objects.get(id=id)
    
    def resolve_review(self, info, id):
        return review.Review.objects.get(id=id)

    def resolve_visitor(self, info, **kwargs):
        return visitor.Visitor.objects.all()


schema = graphene.Schema(query=Query)