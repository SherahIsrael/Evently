from django.db import models
from django.contrib.auth.models import User


class usersTable(models.Model):
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, null=False)
    dateOfBirth = models.DateField()
    registrationDate = models.DateField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class eventsTable(models.Model):
    eventName = models.CharField(max_length=100, null=False)
    eventDate = models.DateField(null=False)
    startTime = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    attendees = models.ManyToManyField(User, blank=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.eventName}"

# class registrationTable(models.Model):
#   event = models.ForeignKey(eventsTable, blank=True, on_delete=models.CASCADE)
#   user = models.ManyToManyField(usersTable, blank=True, on_delete=models.CASCADE)
