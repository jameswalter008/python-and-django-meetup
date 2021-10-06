from django.db.models.fields import SlugField
import meetup
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Meetup,Participants


# Create your views here.
def index(request):
    meetups=Meetup.objects.all()
    return render(request, 'meetup/index.html',{
        'meetups':meetups
    })

def meetup_details(request,meetup_slug):
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        if request.method=='GET':
            registration_form=RegistrationForm()
        else:
            registeration_form=RegistrationForm(request.POST)
            if registeration_form.is_valid():
                # participant=registeration_form.save()
                user_email=registeration_form.cleaned_data['email']#cleaned data store the key of the value entered by user.
                participant, _=Participants.objects.get_or_create(email=user_email)#get_or_create method returns a tuple/ participant is create or identify the existing data and another is was_created which tell us the user entries is created or not
                selected_meetup.participants.add(participant)
                return redirect('confirmed',meetup_slug=meetup_slug)

        return render(request,'meetup/meetupdetail.html',{
                'meetup_found':True,
                'meetup':selected_meetup,
                'form':registration_form
            })

    except Exception as exc:
        print(exc)
        return render(request,'meetup/meetupdetail.html',{
            'meetup_found':False,
        })

def confirmation(request,meetup_slug):
    meetup=Meetup.objects.get(slug=meetup_slug)
    return render(request,"meetup/confirmation.html",{
        'organizer_email':meetup.organizer_email,
        'meetup':meetup
    })
