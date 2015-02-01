from decimal import Decimal

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from .models import Week, Timecard, TimecardObject

class TimecardObjectFormset(BaseInlineFormSet):
    def clean(self):
        '''Check to ensure the proper number of hours are entered'''
        super(TimecardObjectFormset, self).clean()

        if any(self.errors):
            return

        percentage = Decimal(0.0)

        for unit in self.cleaned_data:
            try:
                percentage = percentage + unit["time_percentage"]
            except KeyError:
                pass

        if percentage > 1:
            raise ValidationError('You have entered more than 100%')

        if percentage < 1:
            raise ValidationError('You have entered less than 100%')


class WeekAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')

class TimecardObjectInline(admin.TabularInline):
    model = TimecardObject
    extra = 5
    formset = TimecardObjectFormset

class TimecardAdmin(admin.ModelAdmin):
    list_display = ('week', 'first_name', 'last_name')
    inlines = (TimecardObjectInline,)

admin.site.register(Week, WeekAdmin)
admin.site.register(Timecard, TimecardAdmin)