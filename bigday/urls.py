from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^', include('wedding.urls')),
    url(r'^', include('guests.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url('^accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
