from meetup.models import Meetup,Location,Participants
from django.contrib import admin

# Register your models here.
class MeetupAdmin(admin.ModelAdmin):
    list_display=('title','date','location') 
    list_filter=('location','date')
    prepopulated_fields={'slug':('title',)}


admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participants)
