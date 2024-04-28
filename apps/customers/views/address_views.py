from utils.responses.main import Response
from rest_framework.views import APIView
from utils.decorators.authorization import is_authorize
from apps.customers.service import CustomerService
from apps.customers.selector import CustomerSelector

class CustomerAddressAPI(APIView):

    @is_authorize
    def get(self,request):
        token_data=request.token_data
        message,status=CustomerSelector.get_address(token_data.get('user'))
        return Response(message,status)

    @is_authorize
    def post(self,request):
        token_data=request.token_data
        message,status=CustomerService.add_address(request,token_data.get('user'))
        return Response(message,status)

    def patch(self,request):
        pass

    def delete(self,request):
        pass