from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Quiz, UserSession, UserResponse


def home(request):
    quizzes = Quiz.objects.filter(is_active=True)
    return render(request, 'surveys/home.html', {'quizzes': quizzes})


def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    session = UserSession.objects.create(quiz=quiz)
    request.session['quiz_session_id'] = session.id
    request.session['question_index'] = 0
    return redirect('quiz_question', quiz_id=quiz.id)


def quiz_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    session_id = request.session.get('quiz_session_id')

    if not session_id:
        return redirect('home')

    session = get_object_or_404(UserSession, id=session_id)
    questions = list(quiz.questions.all())
    index = request.session.get('question_index', 0)

    if index >= len(questions):
        session.finished_at = timezone.now()
        session.calculate_score()
        return redirect('quiz_results', session_id=session.id)

    question = questions[index]

    if request.method == 'POST':
        answer_id = request.POST.get('answer')

        if not answer_id:
            return render(request, 'surveys/quiz.html', {
                'question': question,
                'quiz': quiz,
                'index': index + 1,
                'total': len(questions),
                'error': 'Пожалуйста, выберите ответ!',
            })

        UserResponse.objects.create(
            session=session,
            question=question,
            selected_answer_id=answer_id,
        )
        request.session['question_index'] = index + 1
        return redirect('quiz_question', quiz_id=quiz.id)

    return render(request, 'surveys/quiz.html', {
        'question': question,
        'quiz': quiz,
        'index': index + 1,
        'total': len(questions),
    })


def quiz_results(request, session_id):
    session = get_object_or_404(UserSession, id=session_id)
    responses = session.responses.select_related('question',
                                                   'selected_answer')
    return render(request, 'surveys/results.html', {
        'session': session,
        'responses': responses,
    })
from django.http import JsonResponse

def api_quizzes(request):
    quizzes = Quiz.objects.filter(is_active=True).values('id', 'title', 'description')
    return JsonResponse(list(quizzes), safe=False)

def api_quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    return JsonResponse({'id': quiz.id, 'title': quiz.title, 'description': quiz.description})