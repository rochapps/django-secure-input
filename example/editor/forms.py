from django import forms

from secure_input.fields import SecureCharFieldInput
from secure_input.widgets import WYSIWYGWidget
from .models import Comment

__all__ = ('SecureCommentForm', 'SecureWYSIWYGCommentForm', )


class SecureCommentForm(forms.ModelForm):
    comment = SecureCharFieldInput()

    class Meta:
        model = Comment


class SecureWYSIWYGCommentForm(forms.ModelForm):
    comment = SecureCharFieldInput(widget=WYSIWYGWidget)

    class Meta:
        model = Comment