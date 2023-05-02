import graphene
from coffeehouse.schema import *
from coffeehouse.models import coffeeshop, category, freetable, ingredient, order, orderitem, product, promotion, review, visitor


class Query(graphene.ObjectType):
    coffeeshop = graphene.Field(CoffeeShopType, id=graphene.ID(required=True))
    category = graphene.Field(CategoryType, id=graphene.ID(required=True))
    freetable = graphene.Field(FreeTableType)
    ingredient = graphene.Field(IngredientType)
    order = graphene.Field(OrderType)
    orderitem = graphene.Field(OrderItemType)
    product = graphene.Field(ProductType)
    promotion = graphene.Field(PromotionType)
    review = graphene.Field(ReviewType)
    visitor = graphene.Field(VisitorType)
    

    def resolve_coffeeshop(self, info, id):
        return coffeeshop.CoffeeShop.objects.get(id=id)
    
    def resolve_category(self, info, id):
        return category.Category.objects.get(id=id)
    
    def resolve_freetable(self, info, id):
        return freetable.FreeTable.objects.all()
    
    def resolve_ingredient(self, info, id):
        return ingredient.Ingredient.objects.all()
    
    def resolve_order(self, info, id):
        return order.Order.objects.all()
    
    def resolve_orderitem(self, info, id):
        return orderitem.Order.objects.all()
    
    def resolve_product(self, info, id):
        return product.Product.objects.all()
    
    def resolve_promotion(self, info, id):
        return promotion.Promotion.objects.all()
    
    def resolve_review(self, info, id):
        return review.Review.objects.all()

    def resolve_visitor(self, info, **kwargs ):
        return visitor.Visitor.objects.all()


schema = graphene.Schema(query=Query)