from django.urls import path

from .views import *

app_name = "pages"

urlpatterns = [
    path('about', AboutView.as_view(), name="about"),
]