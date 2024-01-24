from django.shortcuts import render
from trivia.models import Question

def home(request):
    allQuestions= Question.objects.all()
    context= {
        'allQuestions': allQuestions }
    return render(request, 'trivia/home.html', context, )

def question_index(request, pk):
    questionsPK = Question.objects.get(pk=pk)
    if request.method == 'POST':
        questions=Question.objects.all()
        result=0
        if questionsPK.option1 is not None:
            if questionsPK.correct_answer == request.POST.get(questionsPK.question):
                result="Correct answer!"
            else:
                result="Wrong answer, try again!"
            context = {
                'questionsPK':questionsPK,
                'result':result,
            }
        return render(request, "trivia/question_index.html", context)
    else:
        questions = Question.objects.all()
        questionsPK = Question.objects.get(pk=pk)
        context = {
            'questions':questions,
            'questionsPK':questionsPK
        }
        return render(request, "trivia/question_index.html", context)
