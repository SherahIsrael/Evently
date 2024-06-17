from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# class usersTable(AbstractUser):
#     firstName = models.CharField(max_length=50, null=False)
#     lastName = models.CharField(max_length=50)
#     email = models.EmailField(max_length=150, null=False)
#     dateOfBirth = models.DateField()
#     registrationDate = models.DateField(auto_now_add=True)
#     slug = models.SlugField(default="", null=False)

#     def __str__(self):
#         return f"{self.firstName} {self.lastName}"
class usersTable(AbstractUser):
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    registrationDate = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="", null=False)
    username = models.CharField(max_length=150, default="temporary_username")
    password = models.CharField(max_length=260, default="password")
    last_name = models.CharField(max_length=50, default="")
    
    REQUIRED_FIELDS = ["username","password", "registrationDate"]
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class eventsTable(models.Model):
    eventName = models.CharField(max_length=100, null=False)
    eventDate = models.DateField(null=False)
    startTime = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.eventName}"

# class registrationTable(models.Model):
#   event = models.ForeignKey(eventsTable, blank=True, on_delete=models.CASCADE)
#   user = models.ManyToManyField(usersTable, blank=True, on_delete=models.CASCADE)
