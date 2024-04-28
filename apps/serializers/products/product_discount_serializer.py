from rest_framework import serializers
from apps.models import ProductDiscount
from benedict import benedict

class ProductDiscountOutSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDiscount
        fields=('uid','discount_name','discount_desc','discount_percentage')

class ProductDiscountInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    discount_name=serializers.CharField()
    discount_desc=serializers.CharField(required=False)
    discount_percentage=serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate(self,data):
        return benedict(data)