from rest_framework import serializers
from apps.models import ProductBrand
from benedict import benedict

class ProductBrandOutSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductBrand
        fields=('uid','brand_name','image')

class ProductBrandInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    brand_name=serializers.CharField()
    image=serializers.FileField(required=False)

    def validate(self,data):
        return benedict(data)

