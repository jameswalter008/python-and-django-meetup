from django.urls import path
from . import views

urlpatterns=[
    path('meetups/',views.index,name='all-meetups'),#our-domain.com/meetups
    path('meetups/<slug:meetup_slug>/registered',views.confirmation,name="confirmed"),#our-domain.com/meetups/<dynamic-path-segment>
    path('meetups/<slug:meetup_slug>',views.meetup_details,name='meetup-details'),#our-domain.com/meetups/<dynamic-path-segment>
]