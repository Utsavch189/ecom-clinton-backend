from rest_framework import serializers
from apps.models import ProductInventory
from benedict import benedict

class ProductInventoryOutSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductInventory
        fields=('uid','quantity')

class ProductInventoryInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    quantity=serializers.IntegerField()

    def validate(self,data):
        return benedict(data)