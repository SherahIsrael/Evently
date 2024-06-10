from django.urls import path
from . import views


# app_name = "eventure"
urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('users/', views.users, name='users'),
    path('users/details/<int:id>', views.details, name='details'),
    path('events_json/<int:year>/<int:month>/', views.events_json, name='events_json'),
]
