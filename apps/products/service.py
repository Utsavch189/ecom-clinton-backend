from rest_framework import status
from apps.models import (
    ProductCategory,
    Product,
    VariantOptions,
    VarientAttribute,
    ProductVarient,
    ProductInventory,
    ProductDiscount,
    ProductBrand,
    ProductAttachment
    )
from apps.serializers.products.product_serializer import ProductInputSerializer,ProductOutputSerializer
from django.db import transaction
from utils.id_generate.main import generate_id
from utils.decorators.schema_validate import schema_validate
from django.conf import settings

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

class ProductService:

    @staticmethod
    @schema_validate(schema_name=f'{settings.BASE_DIR}/apps/products/schemas/add_product.json')
    def add_product(request)->tuple:
        serializers=ProductInputSerializer(data=request.data)
        if serializers.is_valid():
            data:ProductInputSerializer=serializers.validated_data
            
            with transaction.atomic():
                product_category=ProductCategory.objects.get(uid=data.product_category.uid)
                product_brand=ProductBrand.objects.get(uid=data.product_brand.uid)
                if data.get('product_discount'):
                    product_discount=data.product_discount
                else:
                    product_discount=None
                product=Product(
                    uid=generate_id(),
                    product_name=data.product_name,
                    product_brand=product_brand,
                    product_category=product_category,
                    product_desc=data.product_desc,
                    product_price=data.product_price,
                    product_discount=product_discount
                )
                product.save()

                product_varients=data.product_varients

                for varients in product_varients:
                    if varients.get('desc'):
                        desc=varients.desc
                    else:
                        desc=""
                    
                    if varients.get('varient_discount'):
                        varient_discount=varients.varient_discount
                    else:
                        varient_discount=None
                    
                    product_inventory=ProductInventory(
                        uid=generate_id(),
                        quantity=varients.product_inventory.quantity
                    )
                    product_inventory.save()

                    product_varient=ProductVarient(
                        uid=generate_id(),
                        desc=desc,
                        product=product,
                        varient_discount=varient_discount,
                        product_inventory=product_inventory,
                        product_price_adjustment=varients.product_price_adjustment
                    )
                    product_varient.save()

                    varient_attributes=varients.varient_attributes

                    for attrs in varient_attributes:
                        varient_attribute=VarientAttribute(
                            uid=generate_id(),
                            varient=product_varient,
                            options=VariantOptions.objects.get(uid=attrs.option),
                            value=attrs.value
                        )
                        varient_attribute.save()
                    
                    if varients.get('product_attachments'):
                        # set images 
                        pass

                return (
                    {"message":"product is created!","product":ProductOutputSerializer(instance=product).data},
                    status.HTTP_201_CREATED
                )
        else:
            print(serializers.errors)
            return (
                {"message":serializers.errors},
                status.HTTP_400_BAD_REQUEST
            )