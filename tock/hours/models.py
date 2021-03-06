from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from projects.models import Project

# Create your models here.
class ReportingPeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    working_hours = models.PositiveSmallIntegerField(default=40,
                            validators=[MaxValueValidator(40)])

    def __str__(self):
        return str(self.start_date)

    class Meta:
        verbose_name = "Reporting Period"
        verbose_name_plural = "Reporting Periods"

class Timecard(models.Model):
    user = models.ForeignKey(User)
    reporting_period = models.ForeignKey(ReportingPeriod)
    time_spent = models.ManyToManyField(Project, through='TimecardObject')

    class Meta:
        unique_together = ('user', 'reporting_period')

class TimecardObject(models.Model):
    timecard = models.ForeignKey(Timecard)
    project = models.ForeignKey(Project)
    time_percentage = models.DecimalField(decimal_places=0, max_digits=3, validators=[MaxValueValidator(100)])
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
