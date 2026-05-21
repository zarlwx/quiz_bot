from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/<int:quiz_id>/start/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:quiz_id>/', views.quiz_question, name='quiz_question'),
    path('results/<int:session_id>/', views.quiz_results, name='quiz_results'),
    path('api/quizzes/', views.api_quizzes, name='api_quizzes'),
    path('api/quiz/<int:quiz_id>/', views.api_quiz_detail, name='api_quiz_detail'),
]