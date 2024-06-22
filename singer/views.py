from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import  FormView
from singer.forms import *


# Create your views here.
class WelcomeView(TemplateView):
    template_name = "singer/welcome.html"
    

class LoginView(FormView):
    template_name = "singer/login.html"
    
    form_class = SingerLoginForm