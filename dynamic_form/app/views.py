# from django.shortcuts import render, get_object_or_404, redirect
from .models import Survey, SurveyResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import (CreateView, UpdateView)
from dynamic_forms.views import DynamicFormMixin
# Create your views here.


class SurveyListView(ListView):
    """
    Creates the survey list view which doubles as the home page.
    A list of all survey forms
    """
    model = Survey

    def get_queryset(self):
        return Survey.objects.all()


class SurveyDetailView(DetailView):
    """
    Renders a detailed view of a selected survey and all responses to survey if any exist
    """
    model = Survey
    pk_url_kwarg = "survey_id"


class CreateSurveyView(LoginRequiredMixin, CreateView):
    """
    Create a new survey form using the django dynamic form
    """
    login_url = '/login/'
    model = Survey
    fields = ['form_title', 'description', 'form']
    template_name = "app/survey_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('app:survey_detail', kwargs={"survey_id": self.object.pk})


class SurveyEditView(UpdateView):
    """
    Edit an existing survey
    """
    model = Survey
    fields = '__all__'
    pk_url_kwarg = "survey_id"

    def get_success_url(self):
        return reverse('app:survey_detail', kwargs={"survey_id": self.object.pk})


class RespondView(DynamicFormMixin, CreateView):
    """
    this view allows end users to respond ie fill dynamically generated forms
    """
    model = SurveyResponse
    fields = ['response']
    template_name = "app/respond.html"

    form_model = Survey
    form_pk_url_kwarg = "survey_id"
    response_form_fk_field = "survey"
    response_field = "response"

    def get_success_url(self):
        return reverse('app:survey_detail', kwargs={"survey_id": self.form_instance.pk})
