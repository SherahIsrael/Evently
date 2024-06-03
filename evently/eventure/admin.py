from django.contrib import admin
from .models import usersTable
from .models import eventsTable

# Register your models here.
admin.site.register(usersTable)
admin.site.register(eventsTable)
