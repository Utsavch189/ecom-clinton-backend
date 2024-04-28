from utils.responses.main import Response
from rest_framework.views import APIView
from utils.decorators.authorization import is_authorize
from apps.customers.service import CustomerService
from apps.customers.selector import CustomerSelector

class CustomerAPI(APIView):

    @is_authorize
    def get(self,request):
        token_data=request.token_data
        message,status=CustomerSelector.get_user(token_data.get('user'))
        return Response(message,status)

    def patch(self,request):
        pass

    def delete(self,request):
        pass