from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

def users(request):
  allusers = usersTable.objects.all().values()
  template = loader.get_template('users.html')
  context = {
    'allusers': allusers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  allusers = usersTable.objects.get(id=id)
  template = loader.get_template('usersdetails.html')
  context = {
    'allusers': allusers,
  }
  return HttpResponse(template.render(context, request))

