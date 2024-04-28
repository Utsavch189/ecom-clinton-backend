from rest_framework import serializers
from apps.models import VarientAttribute
from .varient_options_serializer import VariantOptionsOutSerializer
from benedict import benedict
from apps.models import VariantOptions

class VarientAttributeOutSerializer(serializers.ModelSerializer):
    options=VariantOptionsOutSerializer(many=False)

    class Meta:
        model=VarientAttribute
        fields=('options','value')


class VarientAttributeInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    varient=serializers.CharField(required=False)
    option=serializers.CharField()
    value=serializers.CharField()

    def validate_option(self, data):
        if not VariantOptions.objects.filter(uid=data).exists():
            raise serializers.ValidationError('option is invalid!')
        return data

    def validate(self, attrs):
        return benedict(attrs)