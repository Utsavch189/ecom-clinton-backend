from rest_framework import serializers
from benedict import benedict
from apps.models import Product
from .product_category_serializer import ProductCategoryInSerializer,ProductCategoryOutSerializer
from .product_discount_serializer import ProductDiscountInSerializer,ProductDiscountOutSerializer
from .product_varient_serializer import ProductVarientOutputSerializer,ProductVarientInputSerializer
from .product_brand_serializer import ProductBrandInSerializer,ProductBrandOutSerializer

class ProductOutputSerializer(serializers.ModelSerializer):
    product_category=ProductCategoryOutSerializer(many=False)
    product_varients=ProductVarientOutputSerializer(many=True,source='product_varient')
    product_discount=ProductDiscountOutSerializer(many=False)
    product_brand=ProductBrandOutSerializer(many=False)
    class Meta:
        model=Product
        fields=('uid','product_name','product_brand','product_category','product_discount','product_desc','product_price','product_varients','is_active','created_at','modified_at','deleted_at')

class ProductInputSerializer(serializers.Serializer):
    """
    {
    "product_name":"Redmi Note 10s",
    "product_brand":{
        "uid":"9e914687c7ca45758e83c77fac3dfa34171359380352000",
        "brand_name":"XAOMI"
    },
    "product_category":{
        "uid":"10d17b08fbb044c9bb788f651f7aed08171359380357423",
        "category_name":"SMARTPHONE"
    },
    "product_desc":"Excelent Smart Phone",
    "product_price":"98000",
    // "product_discount":"",
    "product_varients":[
        {
            "product_inventory":{
                "quantity":40
            },
            // "varient_discount":"",
            // "desc":"",
            "product_price_adjustment":10000,
            "product_attachments":[],
            "varient_attributes":[
                {
                    "option":"f6f14b2bda6f4ee4s9b52462e65082081171359380365596",
                    "value":"128gb"
                },
                {
                    "option":"f6f14b2bda6f4ee49b52462e65082081171359380365596",
                    "value":"white"
                }
            ]
        }
    ]
}
    """
    uid=serializers.CharField(required=False)
    product_name=serializers.CharField()
    product_brand=ProductBrandInSerializer(many=False)
    product_category=ProductCategoryInSerializer(many=False)
    product_desc=serializers.CharField()
    product_price=serializers.DecimalField(max_digits=10, decimal_places=2)
    product_discount=ProductDiscountInSerializer(many=False,required=False)
    product_varients=ProductVarientInputSerializer(many=True)

    def validate(self,data):
        return benedict(data)