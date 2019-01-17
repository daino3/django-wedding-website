from django.conf import settings
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP
from .models import Photo, SiteSection
from .serializers import PhotoSerializer, SiteSectionSerializer
from datetime import date


def home(request):
    photos = Photo.objects.all()
    sections = SiteSection.objects.all().order_by('order')

    photo_data = PhotoSerializer(photos, many=True).data
    section_data = SiteSectionSerializer(sections, many=True).data

    wedding_day = date(2019, 9, 15)
    today = date.today()

    days_until_wedding = (wedding_day - today).days

    section_test = {
        section['order']: section['content']
        for section in section_data
    }

    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'photos': {photo['name']: photo for photo in photo_data},
        'days_until_wedding': days_until_wedding,
        'sections': section_test,
    })
