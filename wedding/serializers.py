from rest_framework import serializers

from .models import Photo, SiteSection


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        depth = 0
        fields = '__all__'


class SiteSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSection
        depth = 0
        fields = '__all__'