from django.conf.urls import url

from guests import views

urlpatterns = [
    url(r'^guests/$', views.GuestListView.as_view(), name='guest-list'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^guests/export$', views.export_guests, name='export-guest-list'),
    url(r'^invite/(?P<invite_id>[\w-]+)/$', views.invitation, name='invitation'),
    url(r'^invite-email/(?P<invite_id>[\w-]+)/$', views.invitation_email_preview, name='invitation-email'),
    url(r'^invite-email-test/(?P<invite_id>[\w-]+)/$', views.invitation_email_test, name='invitation-email-test'),
    url(r'^save-the-date/$', views.save_the_date_random, name='save-the-date-random'),
    url(r'^save-the-date/(?P<template_id>[\w-]+)/$', views.save_the_date_preview, name='save-the-date'),
    url(r'^email-test/(?P<template_id>[\w-]+)/$', views.test_email, name='test-email'),
    url(r'^rsvp/confirm/(?P<invite_id>[\w-]+)/$', views.rsvp_confirm, name='rsvp-confirm'),
]
