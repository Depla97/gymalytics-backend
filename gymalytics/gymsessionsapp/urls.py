from django.urls import path
from . import views

urlpatterns = [
    path("athlete/<int:id>/", views.manageAthletes.as_view(), name="athletes"),
    path("athlete/", views.createAthletes.as_view(), name="athletes"),
]
