from django import forms
from .models import Suggestion


class PostForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['title', 'describe']
        labels = {
            'title': '▶ 약속 제목 (50자 이내)',
            'describe': '▶ 약속 내용'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input'
            }),
            'describe': forms.Textarea(attrs={
                'class': 'input',
                'style': 'height: 40vh'
            }),
        }
