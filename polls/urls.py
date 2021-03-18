"""Polls app URL."""
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('question/add/',
         login_required(views.CreateQuestionView.as_view()),
         name='create-question'),
    path('<int:pk>/choice/add/',
         login_required(views.CreateChoiceView.as_view()),
         name='create-choice'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
