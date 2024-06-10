from django.contrib import admin
from .models import usersTable
from .models import eventsTable


class usersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("firstName", "lastName")}


# Register your models here.
admin.site.register(usersTable, usersAdmin)
admin.site.register(eventsTable)
