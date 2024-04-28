from utils.responses.main import Response
from rest_framework.views import APIView
from utils.decorators.authorization import is_authorize
from .selector import ProductSelector
from apps.serializers.products import product_serializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .service import ProductService

class ProductAPI(APIView):

    @swagger_auto_schema(       
        manual_parameters=[
            openapi.Parameter('page', openapi.IN_QUERY, description="Page number", type=openapi.TYPE_INTEGER),
            openapi.Parameter('page-size', openapi.IN_QUERY, description="Number of items per page", type=openapi.TYPE_INTEGER),
            openapi.Parameter('category', openapi.IN_QUERY, description="Product category", type=openapi.TYPE_STRING),
            openapi.Parameter('product_id', openapi.IN_QUERY, description="ID of the product", type=openapi.TYPE_STRING)
        ],
        tags=["Products"],
        responses={200: product_serializer.ProductOutputSerializer(many=True), 400: 'Bad Request'},
        operation_description="""Retrieve a list of products or a single product \n
                                1. /api/v1/product/?page-size=4&page=1&category=3406cb9d-d734-426c-b676-7cfc1f46c33a17113572528303 \n
                                2. /api/v1/product/?page-size=4&page=1 \n
                                3. /api/v1/product/?product_id=3406cb9d-d734-426c-b676-7cfc1f46c33a17113572528303
                                """
    )
    
    def get(self,request):
        query_params=request.query_params
        data,status=ProductSelector.get_product(
            # page_size=query_params.get('page-size'),
            # page=query_params.get('page'),
            # category_id=query_params.get('category'),
            # product_id=query_params.get('product_id')
            query_params=query_params
        )
        return Response(data,status=status)
    

    @swagger_auto_schema(       
        responses={201: product_serializer.ProductOutputSerializer(many=False), 400: 'Bad Request'},
        operation_description="""Create Products""",
        security=[{"Bearer": []}],
        parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="Authorization Header", type=openapi.TYPE_STRING),
        ],
        tags=["Products"],
        request_body=product_serializer.ProductInputSerializer(many=False)
    )

    def post(self,request):
        message,status=ProductService.add_product(request)
        return Response(message,status=status)