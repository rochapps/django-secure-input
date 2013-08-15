from django import forms

from secure_input.fields import SafeCharFieldInput, WYSIWYGField, MiniWYSIWYGField
from .models import Comment

__all__ = ('SecureCommentForm', 'SecureWYSIWYGCommentForm', )


class SecureCommentForm(forms.ModelForm):
    comment = SafeCharFieldInput()

    class Meta:
        model = Comment


class SecureWYSIWYGCommentForm(forms.ModelForm):
    comment = WYSIWYGField()

    class Meta:
        model = Comment


class SecureMiniWYSIWYGCommentForm(forms.ModelForm):
    comment = MiniWYSIWYGField()

    class Meta:
        model = Comment