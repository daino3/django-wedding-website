from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        depth = 0
        fields = '__all__'
