from rest_framework import serializers
from apps.models import ProductCategory
from benedict import benedict

class ProductCategoryOutSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields=('uid','category_name')

class ProductCategoryInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    category_name=serializers.CharField()

    def validate(self,data):
        return benedict(data)

