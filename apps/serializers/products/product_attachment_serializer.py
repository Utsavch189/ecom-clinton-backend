from rest_framework import serializers
from apps.models import ProductAttachment
from benedict import benedict

class ProductAttachmentOutSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductAttachment
        fields='__all__'

class ProductAttachmentInSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    file=serializers.FileField()
    caption=serializers.CharField()

    def validate(self,data):
        return benedict(data)