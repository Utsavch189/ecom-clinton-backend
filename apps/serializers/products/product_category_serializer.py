from rest_framework import serializers
from apps.models import ProductCategory
from benedict import benedict
from .varient_options_serializer import VariantOptionsOutSerializer

class ProductCategoryOutSerializer(serializers.ModelSerializer):
    varients=VariantOptionsOutSerializer(many=True,source='category_variants')
    class Meta:
        model=ProductCategory
        fields=('uid','category_name','varients')

class ProductCategoryInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    category_name=serializers.CharField()

    def validate(self,data):
        return benedict(data)

