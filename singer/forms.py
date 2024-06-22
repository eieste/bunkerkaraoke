from django import forms
from singer.models import Singer


class SingerLoginForm(forms.ModelForm):


    class Meta:
        model = Singer
        fields = ["name"]