from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate

from .models import usersTable
from .models import eventsTable

from .forms import SignUpForm, LoginForm


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def events(request):
    allevents = eventsTable.objects.all().values()
    template = loader.get_template("events.html")
    context = {
        "allevents": allevents,
    }
    return HttpResponse(template.render(context, request))


def eventsDetails(request, id):
    allevents = eventsTable.objects.get(id=id)
    template = loader.get_template("eventsdetails.html")
    context = {
        "allevents": allevents,
    }
    return HttpResponse(template.render(context, request))


def users(request):
    allusers = usersTable.objects.all().values()
    template = loader.get_template("users.html")
    context = {
        "allusers": allusers,
    }
    return HttpResponse(template.render(context, request))


def usersDetails(request, identifier):
    try:
        allusers = usersTable.objects.get(slug=identifier)
    except usersTable.DoesNotExist:
        allusers = get_object_or_404(usersTable, id=identifier)
    
    template = loader.get_template("usersdetails.html")
    context = {
        "allusers": allusers,
    }
    return HttpResponse(template.render(context, request))


def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "register/signUp.html", {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'register/login.html', {'form': form})


def events_json(request, year, month):
    events = eventsTable.objects.filter(eventDate__year=year, eventDate__month=month)
    events_data = [{"day": event.eventDate.day, "name": event.eventName} for event in events]
    return JsonResponse(events_data, safe=False)
