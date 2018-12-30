from django.conf import settings
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP
from .models import Photo
from .serializers import PhotoSerializer


def home(request):
    photos = Photo.objects.all()

    photo_data = PhotoSerializer(photos, many=True).data

    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'photos': {photo['name']: photo for photo in photo_data}
    })
