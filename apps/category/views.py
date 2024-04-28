from utils.responses.main import Response
from rest_framework.views import APIView
from utils.decorators.authorization import is_authorize
from .selector import CategorySelector

class CategoryAPI(APIView):

    def get(self,request):
        query_params=request.query_params
        if query_params.get('uid'):
            message,status=CategorySelector.get_a_category(query_params.get('uid'))
        elif query_params.get('page') and query_params.get('page-size'):
            message,status=CategorySelector.get_categories(query_params.get('page'),query_params.get('page-size'))
        else:
            raise Exception("uid or page and page-size should be present in params!")
        return Response(message,status)
    
    def post(self,request):
        pass

    def patch(self,request):
        pass

    def delete(self,request):
        pass