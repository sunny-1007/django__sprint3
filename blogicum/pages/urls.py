from django.urls import path
from pages import views


urlpatterns = [
    path("about/", views.about, name="about"),
    path("rules/", views.rules, name="rules"),
]
