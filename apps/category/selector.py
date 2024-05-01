from apps.serializers.products.product_category_serializer import ProductCategoryOutSerializer
from apps.models import ProductCategory
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from rest_framework import status
from utils.exceptions import main

class CategorySelector:

    @staticmethod
    def get_a_category(id:int)->tuple:
        if not ProductCategory.objects.filter(uid=id).exists():
            raise main.NotExists(detail="category doesn't exists!")
        catgegory=ProductCategory.objects.get(uid=id)
        return (
            {"category":ProductCategoryOutSerializer(instance=catgegory,many=False).data},
            status.HTTP_200_OK
        )

    @staticmethod
    def get_categories(page:int,page_size:int)->tuple:
        categories=ProductCategory.objects.all()
        paginator=Paginator(categories,page_size)
        try:
            categories=paginator.page(page)
        except PageNotAnInteger:
            categories=paginator.page(1)
        except EmptyPage:
            categories=[]
        return (
            {"categories":ProductCategoryOutSerializer(instance=categories,many=True).data},
            status.HTTP_200_OK
        )
