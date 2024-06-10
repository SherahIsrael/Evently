from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from .models import usersTable
from .models import eventsTable


def home(request):
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
    return render(request, 'home.html')


def events(request):
    allevents = eventsTable.objects.all().values()
    template = loader.get_template('events.html')
    context = {
        'allevents': allevents,
    }
    return HttpResponse(template.render(context, request))


def eventsDetails(request, id):
    allevents = eventsTable.objects.get(id=id)
    template = loader.get_template('eventsdetails.html')
    context = {
        'allevents': allevents,
    }
    return HttpResponse(template.render(context, request))


def users(request):
    allusers = usersTable.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'allusers': allusers,
    }
    return HttpResponse(template.render(context, request))


def usersDetails(request, slug):
    allusers = usersTable.objects.get(slug=slug)
    template = loader.get_template('usersdetails.html')
    context = {
        'allusers': allusers,
    }
    return HttpResponse(template.render(context, request))


def events_json(request, year, month):
    events = eventsTable.objects.filter(eventDate__year=year, eventDate__month=month)
    events_data = [{'day': event.eventDate.day, 'name': event.eventName} for event in events]
    return JsonResponse(events_data, safe=False)
