from rest_framework import serializers
from apps.models import ProductCategory
from benedict import benedict
from .varient_options_serializer import VariantOptionsOutSerializer,VariantOptionsInSerializer
from .product_brand_serializer import ProductBrandOutSerializer,ProductBrandInSerializer

class ProductCategoryOutSerializer(serializers.ModelSerializer):
    varients=VariantOptionsOutSerializer(many=True,source='category_variants')
    brands=ProductBrandOutSerializer(many=True,source='brand_category')
    class Meta:
        model=ProductCategory
        fields=('uid','category_name','image','varients','brands')

class ProductCategoryInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    image=serializers.FileField(required=False)
    category_name=serializers.CharField()
    varients=VariantOptionsInSerializer(many=True,required=False)
    brands=ProductBrandInSerializer(many=True,required=False)

    def validate(self,data):
        return benedict(data)

