from django.urls import path

from .views import HomePageView, AboutPageView, reservation_list, protected_view

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("protected/", protected_view, name="protected"),
    path("reservations/", reservation_list, name="reservations"),
]
