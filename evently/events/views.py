from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import usersTable

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