from apps.serializers.products.product_serializer import ProductOutputSerializer
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from apps.models import Product
from rest_framework import status
from utils.exceptions import main
from django.db.models import Q

class ProductSelector:

    @staticmethod
    def get_product(query_params:dict):
        filters=Q()
        filters&=Q(is_active=True)

        if 'product_name' in query_params:
            filters&=Q(product_name=query_params['product_name'])
        
        if 'pid' in query_params:
            filters&=Q(uid=query_params['pid'])
        
        if 'product_brand' in query_params:
            filters&=Q(product_brand=query_params['product_brand'])
        
        if 'product_category' in query_params:
            filters&=Q(product_category=query_params['product_category'])
        
        if 'product_price' in query_params:
            filters&=Q(product_price=query_params['product_price'])
        
        if 'max_price' in query_params and 'min_price' in query_params:
            filters&=Q(product_price__range=(query_params['min_price'],query_params['max_price']))

        if filters:
            products=Product.objects.filter(filters)
        else:
            products=Product.objects.filter(is_active=True).order_by('created_at')

        if 'page-size' in query_params and 'page' in query_params:
            paginator=Paginator(products,int(query_params['page-size']))

            try:
                products=paginator.page(int(query_params['page']))
            except PageNotAnInteger:
                products=paginator.page(1)
            except EmptyPage:
                products=[]

        products=ProductOutputSerializer(instance=products,many=True).data

        return (
            {"product":products},
            status.HTTP_200_OK
        )
        
