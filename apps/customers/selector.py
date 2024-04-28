from apps.serializers.user.user_serializer import UserAddressOutputSerializer,UserOutputSerializer
from apps.models import User,UserAddress
from utils.exceptions import main
from rest_framework import status

class CustomerSelector:

    @staticmethod
    def get_address(user_id:str)->tuple:

        if User.objects.filter(uid=user_id).exists():
            main.NotExists(detail="user doesn't exists!")
        
        user=User.objects.get(uid=user_id)

        address=UserAddress.objects.filter(user=user)

        return (
            {"adresses":UserAddressOutputSerializer(instance=address,many=True).data},
            status.HTTP_200_OK
        )
    
    @staticmethod
    def get_user(user_id:str)->tuple:

        if User.objects.filter(uid=user_id).exists():
            main.NotExists(detail="user doesn't exists!")
        
        user=User.objects.get(uid=user_id)

        return (
            {"adresses":UserOutputSerializer(instance=user,many=False).data},
            status.HTTP_200_OK
        )