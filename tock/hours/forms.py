from django import forms
from django.forms.models import inlineformset_factory

from .models import Timecard, TimecardObject

class TimecardForm(forms.ModelForm):
    class Meta:
        model = Timecard
        exclude = ['time_spent', 'reporting_period', 'user']

class TimecardObjectForm(forms.ModelForm):
    class Meta:
        model = TimecardObject
        fields = ['project', 'time_percentage']

TimecardFormSet = inlineformset_factory(Timecard, TimecardObject)