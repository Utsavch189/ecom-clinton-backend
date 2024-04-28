from apps.models import User,UserAddress
from utils.exceptions import main
from apps.serializers.user.user_serializer import UserAddressOutputSerializer,UserAddressInputSerializer
from django.db import transaction
from rest_framework import status
from utils.id_generate.main import generate_id
from utils.decorators.schema_validate import schema_validate
from django.conf import settings

class CustomerService:

    @staticmethod
    @schema_validate(schema_name=f'{settings.BASE_DIR}/apps/customers/schemas/add_address.json')
    def add_address(request:object,user_id:int)->tuple:
        """
        {
            "address_line1":"Guptipara",
            "address_line2":"",
            "city":"Hooghly",
            "postal_code":712512,
            "country":"India"
        }
        """
        data=request.data
        if not User.objects.filter(uid=user_id).exists():
            raise main.NotExists(detail="user doesn't exists!")
        
        user=User.objects.get(uid=user_id)

        if data.get('address_line2')=="":
            data['address_line2']="N/A"

        serializer=UserAddressInputSerializer(data=data)

        if serializer.is_valid():
            data:UserAddressInputSerializer=serializer.validated_data
            address=UserAddress(
                uid=generate_id(),
                user=user,
                address_line1=data.address_line1,
                address_line2=data.address_line2,
                city=data.city,
                postal_code=data.postal_code,
                country=data.country
            )
            address.save()
            return(
                {"message":"address is created!","address":UserAddressOutputSerializer(instance=UserAddress.objects.filter(user=user),many=True).data},
                status.HTTP_201_CREATED
            )
        else:
            return(
                {"message":serializer.errors},
                status.HTTP_400_BAD_REQUEST
            )
