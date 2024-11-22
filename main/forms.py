from .models import Question
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

        label = {
            "question_text": "Write your question here",
        }

        widgets = {
            "question_text": forms.TextInput(attrs={"placeholder": "..."}),
        }
