from utils.responses.main import Response
from rest_framework.views import APIView
from .service import RegisterService,LoginService,RefreshTokenService
from utils.decorators.authorization import is_authorize

class RegisterAPI(APIView):

    def post(self,request):
        message,status=RegisterService.register(request)
        return Response(message,status)

class LoginAPI(APIView):

    def post(self,request):
        message,status=LoginService.login(request)
        return Response(message,status)

class RefreshTokenAPI(APIView):

    @is_authorize
    def get(self,request):
        token_data=request.token_data
        message,status=RefreshTokenService.get_new_token(token_data)
        return Response(message,status)