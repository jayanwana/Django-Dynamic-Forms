from django.contrib import admin
from .models import Survey, SurveyResponse

# Register your models here.
admin.site.register(Survey)
admin.site.register(SurveyResponse)
