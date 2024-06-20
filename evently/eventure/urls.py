from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


# app_name = "eventure"
urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.events, name='events'),
    path("events/details/<int:id>", views.eventsDetails, name="eventDetails"),
    path("users/", views.users, name="users"),
    path("users/details/<str:identifier>/", views.usersDetails, name="userDetails"),
    path("signup/", views.signUp, name="signUp"),
    path("accounts/logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("accounts/login/", views.loginView, name="login"),
    path("events_json/<int:year>/<int:month>/", views.events_json, name="events_json"),
]
