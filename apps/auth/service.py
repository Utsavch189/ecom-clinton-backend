from apps.models import User,UserRole
from apps.serializers.user.user_serializer import UserInputSerializer,UserOutputSerializer
from rest_framework import status
from utils.jwt_builder.main import JwtBuilder
import re
from utils.exceptions import main
from utils.decorators.schema_validate import schema_validate
from django.conf import settings
from django.db import transaction
from utils.id_generate.main import generate_id

class RegisterService:

    @staticmethod
    @schema_validate(schema_name=f'{settings.BASE_DIR}/apps/auth/schemas/register_post.json')
    def register(request):
        """
        "first_name",
        "last_name",
        "email",
        "phone",
        "role",
        "password",
        "confirm_password"
        """
        if not request.data.get('password')==request.data.get('confirm_password'):
            raise main.GenericException(detail='Passwords are not same!',code=400)

        serializer=UserInputSerializer(data=request.data)

        if serializer.is_valid():
            data=serializer.validated_data
            with transaction.atomic():
                user=User(
                    uid=generate_id(),
                    first_name=data.first_name,
                    last_name=data.last_name,
                    email=data.email,
                    password=data.password,
                    phone=data.phone,
                    role=UserRole.objects.filter(role_name=data.role)[0]
                )
                user.save()

                # addresses=data.get('address')
                # for address in addresses:
                #     user_address=UserAddress(
                #         user=user,
                #         address_line1=address.get('address_line1'),
                #         address_line2=address.get('address_line2'),
                #         city=address.get('city'),
                #         postal_code=address.get('postal_code'),
                #         country=address.get('country')
                #     )
                #     user_address.save()

                tokens=JwtBuilder(payload={
                    "user":user.uid,
                    "email":user.email,
                    "role":user.role.role_name
                }).get_token()

                return (
                    {"message":"created successfully!","user":UserOutputSerializer(instance=user).data,"token":tokens},
                    status.HTTP_201_CREATED
                )
        else:
            return (
                {"message":serializer.errors},
                status.HTTP_400_BAD_REQUEST
            )

class LoginService:

    @staticmethod
    @schema_validate(schema_name=f'{settings.BASE_DIR}/apps/auth/schemas/login.json')
    def login(request):
        email=request.data.get('email')
        password=request.data.get('password')

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
            raise main.GenericException(detail="invalid email!")
        
        user=User.objects.filter(email=email)

        if not user:
            raise main.NotExists(detail="email doesn't exists!")
        
        user=user[0]

        if not user.is_correct_password(password):
            raise main.GenericException(detail="wrong password!")
        
        tokens=JwtBuilder(payload={
            "user":user.uid,
            "email":user.email,
            "role":user.role.role_name
        }).get_token()

        return (
            {"message":"tokens are created!","token":tokens},
            status.HTTP_200_OK
        )

class RefreshTokenService:

    @staticmethod
    def get_new_token(payload:dict):
        payload.pop('iat')
        payload.pop('exp')
        tokens=JwtBuilder(payload=payload).get_token()
        print(tokens)
        return (
            {"message":"new tokens are created!","token":tokens},
            status.HTTP_200_OK
        )