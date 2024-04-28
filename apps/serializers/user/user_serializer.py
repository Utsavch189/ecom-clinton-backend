from rest_framework import serializers
from benedict import benedict
from apps.models import User,UserRole,UserAddress

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class UserAddressOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAddress
        fields = '__all__'

class UserAddressInputSerializer(serializers.Serializer):
    address_line1=serializers.CharField()
    address_line2=serializers.CharField(required=False)
    city=serializers.CharField()
    postal_code=serializers.CharField()
    country=serializers.CharField()

    def validate(self, attrs):
        return benedict(attrs)

class UserOutputSerializer(serializers.ModelSerializer):
    role=UserRoleSerializer(many=False)
    address=UserAddressOutputSerializer(many=True,source="users_address") # source='users_address' in UserSerializer refers to the related_name of the UserAddress model's ForeignKey to User.
    class Meta:
        model=User
        fields=['uid','first_name','last_name','email','phone','role','address','is_active','created_at','modified_at','deleted_at']

class UserInputSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    phone=serializers.CharField()
    role=serializers.CharField()
    address=UserAddressInputSerializer(many=True,required=False)
    
    def validate_password(self,value):
        if len(value) != 6:
            raise serializers.ValidationError("password should contains 6 characters!")
        return value
    
    def validate_role(self,value):
        if not UserRole.objects.filter(role_name=value.upper()).exists():
            raise serializers.ValidationError("invalid user role!")
        return value
    
    def validate_phone(self,value):
        if not len(value)==10:
            raise serializers.ValidationError("invalid phone number!")
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("phone number already exists!")
        return value
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already exists!")
        return value

    def validate(self, data):
        return benedict(data)

    
