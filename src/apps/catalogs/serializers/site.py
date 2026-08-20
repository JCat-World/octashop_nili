from rest_framework import serializers

from apps.catalogs.infrastructure.models import LastOffer, Product


# class OptionProductSerializer(serializers.ModelSerializer):
    
    
#     class Meta:
#         model = OptionProduct
#         fields = "__all__"
        

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category')
    # product_image = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='images'
    # )
    class Meta:
        model = Product
        fields = ('id','product_name','category','category_name','company_name','model','product_type',
                #   'product_image'
                  )
        
        
        
        
class ProductLastOfferSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')
    product_category = serializers.CharField(source='product.category.category')
    product_original_price = serializers.CharField(source='product.price')
    # options = OptionProductSerializer(many = True , source = 'product.options')
    
    image = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = LastOffer
        fields = ('id','product','product_name',
                  'product_category','offer_price',
                  'product_original_price','offer_time','image',
                  'options')
        
    def get_image_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.product.images.first().image.url
        return request.build_absolute_uri(photo_url)
        
        
class LastOfferSerializer(serializers.ModelSerializer):
    product_category = serializers.CharField(source='category.title')
    # options = OptionProductSerializer(many = True ,)
    # company_name = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField('get_image_url')
    
    offer_price = serializers.SerializerMethodField()
    sale_price = serializers.SerializerMethodField()
    
    # attributes = serializers.SerializerMethodField()
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.images.first().image.image.url
        return request.build_absolute_uri(photo_url)
    
    def get_offer_price(self, obj):
        if obj.stockrecords.filter(in_offer=True).exists():
            return obj.stockrecords.filter(in_offer=True).first().offer_price
        return None
    
    def get_sale_price(self, obj):
        if obj.stockrecords.filter(in_offer=True).exists():
            return obj.stockrecords.filter(in_offer=True).first().sale_price
        return None

    # def get_company_name(self, obj):
    #     cn = obj.company_name.company_name
    #     return cn
    
    
    # def get_attributes(self, obj):
    #     attributes = {}
    #     for attribute in obj.attributes.all():
    #         attributes[attribute.attribute.name] = attribute.value
    #     return attributes
    
    class Meta:
        model = Product
        # fields = '__all__'
        exclude=(
            "is_public",
            # "balance",
            
        )