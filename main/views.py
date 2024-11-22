from django.shortcuts import render, redirect
from .forms import QuestionForm
from .models import Question


def createQuestionView(request):
    form = QuestionForm
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success_url")
    template_name = "main/question.html"
    context = {"form": form}
    return render(request, template_name, context)


def successView(request):
    return render(request, 'main/success.html')


def listView(request):
    if request.user.is_authenticated:
        obj = Question.objects.all()
        return render(request, 'main/list.html', {"obj": obj})

    return redirect('login_page')
