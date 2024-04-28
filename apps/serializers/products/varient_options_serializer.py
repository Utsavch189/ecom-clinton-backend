from rest_framework import serializers
from benedict import benedict
from apps.models import VariantOptions

class VariantOptionsInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    varient_name=serializers.CharField()

    def validate(self, attrs):
        return benedict(attrs)


class VariantOptionsOutSerializer(serializers.ModelSerializer):
    class Meta:
        model=VariantOptions
        fields=('uid','varient_name')