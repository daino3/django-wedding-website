from django.contrib import admin
from .models import Photo, SiteSection
from django.utils.html import format_html


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'thumbnail')

    def thumbnail(self, obj):
        return format_html('<img style="height:50px;width:auto;" src="{}" />'.format(obj.photo.url))

class SiteSectionAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'section_content')


    def section_content(self, obj):
        iframe = """
            <iframe srcdoc="{}" style="min-height:250px;width:600px;"></iframe>
        """

        return format_html(iframe, obj.content)


    ordering = ('order',)



admin.site.register(Photo, PhotoAdmin)
admin.site.register(SiteSection, SiteSectionAdmin)
