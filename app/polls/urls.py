from django.urls import path
from . import views


urlpatterns = [
    path('polls/', views.polls_list, name='polls_list'),
    path('polls-active/', views.polls_active_list, name='polls_active_list'),
    path('poll-create/', views.poll_create, name='poll_create'),
    path('poll-detail/<int:pk>/', views.poll_detail, name='poll_detail'),
    path('poll-update/<int:pk>/', views.poll_update, name='poll_update'),
    path('poll-delete/<int:pk>/', views.poll_delete, name='poll_delete'),

    path('questions/<int:pk>', views.questions_list, name='questions_list'),
    path('question-create/', views.question_create, name='question_create'),
    path('question-detail/<int:pk>/', views.question_detail, name='question_detail'),
    path('question-update/<int:pk>/', views.question_update, name='question_update'),
    path('question-delete/<int:pk>/', views.question_delete, name='question_delete'),

    path('answer-create/', views.answer_create, name='answer_create'),
    path('answers/<int:pk>/', views.users_answer, name='users_answer'),
]
