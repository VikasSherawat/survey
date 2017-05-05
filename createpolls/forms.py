from django import forms
from .models import Question,Choice

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions


class CreateQuestion(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question',)
        widgets = {
            'question':forms.TextInput(attrs={'class':'input-lg txt-len','placeholder':'Poll Question'}),
            #'question': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        labels = {
            'question': None
        }
