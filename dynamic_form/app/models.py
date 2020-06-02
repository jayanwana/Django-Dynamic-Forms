from django.db import models
from django.contrib.auth.models import User
from dynamic_forms.models import FormField, ResponseField
from django.shortcuts import reverse
# from django.contrib.postgres.fields import JSONField

# Create your models here.


class Survey(models.Model):
    """
    This model handles from creation using FormField from django dynamic forms
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user')
    form_title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    form = FormField()  # this guy here does the heavy lifting

    class Meta:
        verbose_name = 'survey'
        verbose_name_plural = 'surveys'
        ordering = ['form_title']

    def __str__(self):
        return self.form_title

    def get_absolute_url(self):
        return reverse('app:survey_detail', kwargs={'survey_id': self.pk})


class SurveyResponse(models.Model):
    """
        This model allows the storage of responses to forms created by the survey model.
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    response = ResponseField()
