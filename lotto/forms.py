from django import forms
from .models import GuessNumbers


class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',)  #사용자로 부터 받아드릴 data fields
