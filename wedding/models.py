from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Photo(models.Model):
    CHOICES = (
        ('hero', 'Hero'),
        ('story', 'Our Story'),
        ('adler', 'Adler Planetarium'),
        ('wedding_party', 'Wedding Party'),
    )

    description = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=250, null=False, choices=CHOICES)

    photo = models.ImageField(upload_to='photo/uploads', max_length=200, storage=FileSystemStorage())
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SiteSection(models.Model):
    name = models.CharField(max_length=500, null=True)
    order = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(1)])
    content = models.TextField(null=False)



@receiver(pre_save, sender=SiteSection)
def reorder_site_sections(sender, instance, **kwargs):
    sections = [sec for sec in
        SiteSection.objects.all().order_by('order').exclude(id=instance.id)
    ]
    sections.insert(instance.order - 1, instance)
    for i, sec in enumerate(sections):
        if sec.id is None:
            continue
        else:
            # this will not call signals
            SiteSection.objects.filter(id=sec.id).update(order=i+1)
