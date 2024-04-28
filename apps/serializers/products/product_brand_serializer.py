from rest_framework import serializers
from apps.models import ProductBrand
from benedict import benedict

class ProductBrandOutSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductBrand
        fields=('uid','brand_name')

class ProductBrandInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    brand_name=serializers.CharField()

    def validate(self,data):
        return benedict(data)

