from django.urls import include, path
from singer.views import *

app_name = "singer"

urlpatterns = [
    path("start", LoginView.as_view(), name="login"),
    path("", WelcomeView.as_view()),
]
