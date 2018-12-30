from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='wedding', permanent=False)),
    url(r'^wedding$', views.home, name='wedding'),
]
