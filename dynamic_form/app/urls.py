from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('survey/', views.SurveyListView.as_view(), name='survey_list'),
    path('create/', views.CreateSurveyView.as_view(), name='survey_create'),
    path('survey/<int:survey_id>/', views.SurveyDetailView.as_view(), name='survey_detail'),
    path('survey/<int:survey_id>/edit/', views.SurveyEditView.as_view(), name="survey_edit"),
    path('survey/<int:survey_id>/response/', views.RespondView.as_view(), name="survey_respond"),
    path('survey/<int:survey_id>/response/<int:response_id>/', views.RespondView.as_view(), name="response"),
]
