from rest_framework import serializers
from benedict import benedict
from apps.models import ProductVarient
from .product_inventory_serializer import ProductInventoryOutSerializer,ProductInventoryInSerializer
from .product_discount_serializer import ProductDiscountOutSerializer,ProductDiscountInSerializer
from .product_attachment_serializer import ProductAttachmentOutSerializer,ProductAttachmentInSerializer
from .varient_attribute_serializer import VarientAttributeOutSerializer,VarientAttributeInSerializer

class ProductVarientInputSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    desc=serializers.CharField(required=False)
    product_inventory=ProductInventoryInSerializer(many=False)
    varient_discount=ProductDiscountInSerializer(many=False,required=False)
    product_price_adjustment=serializers.DecimalField(max_digits=10, decimal_places=2)
    product_attachments=ProductAttachmentInSerializer(many=True,required=False)
    varient_attributes=VarientAttributeInSerializer(many=True)

    def validate(self, attrs):
        return benedict(attrs)

class ProductVarientOutputSerializer(serializers.ModelSerializer):
    product_inventory=ProductInventoryOutSerializer(many=False)
    varient_discount=ProductDiscountOutSerializer(many=False)
    product_attachments=ProductAttachmentOutSerializer(many=True,source='product_attachment')
    varients=VarientAttributeOutSerializer(many=True,source='product_varient')
    class Meta:
        model=ProductVarient
        fields=('uid','desc','product_inventory','varient_discount','product_price_adjustment','product_attachments','varients')
