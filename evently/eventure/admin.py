from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import usersTable
from .models import eventsTable
# from .forms import SignUpForm, CustomUserChangeForm


class usersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("firstName", "lastName")}


# class CustomUsersAdmin(UserAdmin):
#     add_form = SignUpForm
#     form = CustomUserChangeForm
#     model = usersTable
#     list_display = ["email", "username",]


# Register your models here.
admin.site.register(usersTable, usersAdmin)
admin.site.register(eventsTable)
