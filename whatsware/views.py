from django.http import HttpResponse
from .models import Event,gmaps
from .forms import EventForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth

#form = EventForm()


from django.utils.safestring import mark_safe
from django.template import Library

import json


register = Library()


@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the whatsware index.")

def eventform(request):

    if request.method=='POST':

        evform = EventForm(request.POST)
        print(request.POST)

        if evform.is_valid():
            post = evform.save(commit=False)
            post.timestampAdded = timezone.now()
            post.timestampUpdated = timezone.now()
            coords = gmaps.geocode(post.street+", "+post.city+", "+post.state)
            if coords:
                post.lat=coords[0]['geometry']['location']['lat']
                post.lon=coords[0]['geometry']['location']['lng']
            post.geojsonstring='''
            {"type": "Feature","geometry": {"type": "Point","coordinates": ['''+str(post.lon)+''', '''+str(post.lat)+''']},"properties": {"name": "Dinagat Islands"}}'''
            print("geojson is ", post.geojsonstring)
            post.author = request.user
            post.save()
            sales = Event.objects.all()
            context = {'sales': sales}
            return render(request, 'whatsware/welcome.html', context)
        else:
            return HttpResponse("Form wasn't valid")
    else:
        pass
    evform = EventForm()
    return render(request, 'whatsware/eventform.html', {'evform': evform })

def eventlist(request):
    #a_list = Article.objects.filter(pub_date__year=year)
    sales = Event.objects.all()
    context = {'sales': sales}
    return render(request, 'whatsware/eventlist.html', context)

def welcome(request):
    sales = Event.objects.all()
    context = {'sales': sales }
    return render(request,'whatsware/welcome.html', context)

def map(request):
    sales = Event.objects.all()
    context = {'markers': sales}
    return render(request,'whatsware/map.html')

#remove when done testing
def logo(request):
    sales = Event.objects.all()
    context = {'markers':sales}
    return render(request,'./static/images/neighborhood.svg',context)

#remove when done testing
def mapbox(request):
    sales = Event.objects.all()
    context = {'markers': sales}
    return render(request,'whatsware/mapbox.html',context)

def leaflet(request):
    sales = Event.objects.all()
    context = {'sales': sales}
    return render(request,'whatsware/leaflet.html',context)

def friday(request):
    sales = Event.objects.filter(day__week_day=6)
    context = {'sales': sales}
    return render(request,'whatsware/leaflet.html',context)

def saturday(request):
    sales = Event.objects.filter(day__week_day=7)
    context = {'sales': sales}
    return render(request,'whatsware/leaflet.html',context)

def sunday(request):
    sales = Event.objects.filter(day__week_day=1)
    context = {'sales': sales}
    return render(request,'whatsware/leaflet.html',context)

#def post_detail(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    return render(request, 'blog/post_detail.html', {'post': post})

def filter(request, weekday):
    sales = Event.objects.filter(day__week_day=weekday)
    context = {'sales': sales}
    return render(request,'whatsware/leaflet.html',context)

@login_required
def home(request):
    sales = Event.objects.all()
    context = {'markers': sales}
    return render(request, 'whatsware/home.html', context)

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'whatsware/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'whatsware/password.html', {'form': form})