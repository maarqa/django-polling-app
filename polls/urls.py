from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="Home"),
    path("polls/", views.polls, name="Polls"),
    path('polls/<int:question_id>/', views.details, name='details'),
    path('polls/<int:question_id>/results/', views.result, name='result'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]
