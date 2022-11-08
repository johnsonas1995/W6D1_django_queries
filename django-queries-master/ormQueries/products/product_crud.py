from .models import Product 

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        # print(Product.objects.all())
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model):
        # print(Product.objects.filter(model=model))
        return Product.objects.filter(model=model)[0] #to remove the query set list had to specify index
    
    @classmethod
    def last_record(cls):
        # print(Product.objects.last())
        return Product.objects.last()
    
    @classmethod
    def by_rating(cls, rating):
        # print (Product.objects.filter(rating=rating))
        return Product.objects.filter(rating=rating)
    
    @classmethod
    def by_rating_range(cls, start, end):
        # print (Product.objects.filter(rating__range=[start, end]))
        return Product.objects.filter(rating__range=[start, end])
    
    @classmethod
    def by_rating_and_color(cls, rating, color):
        # print (Product.objects.filter(rating=rating, color=color))
        return Product.objects.filter(rating=rating, color=color)
    
    @classmethod
    def by_rating_or_color(cls, rating, color):
        # print (Product.objects.filter(rating=rating) | Product.objects.filter(color=color))
        return Product.objects.filter(rating=rating) | Product.objects.filter(color=color)
        
    @classmethod
    def no_color_count(cls):
        # print(Product.objects.filter(color__isnull=True).count())
        return Product.objects.filter(color__isnull=True).count()
    
    @classmethod
    def below_price_or_above_rating(cls, top_price, min_rating):
        # print(Product.objects.filter(price_cents__lt=top_price) | Product.objects.filter(rating__gt=min_rating))
        return Product.objects.filter(price_cents__lt=top_price) | Product.objects.filter(rating__gt=min_rating)
    
    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        # print(Product.objects.all().order_by('category', '-price_cents'))
        return Product.objects.all().order_by('category', '-price_cents')
    
    @classmethod
    def products_by_manufacturer_with_name_like(cls, name):
        # print(Product.objects.filter(manufacturer__contains=name))
        return Product.objects.filter(manufacturer__contains=name)
    
    @classmethod
    def manufacturer_names_for_query(cls, name):
        # print(Product.objects.filter(manufacturer__contains=name).values_list('manufacturer',flat=True))
        return Product.objects.filter(manufacturer__contains=name).values_list('manufacturer',flat=True)
    
    