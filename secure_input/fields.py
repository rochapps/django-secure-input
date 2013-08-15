from django import forms

from .widgets import WYSIWYGWidget, MiniWYSIWYGWidget
from .utils import safe_html


class SafeCharFieldInput(forms.CharField):
    """Widget that provides custom clean method to sanitize user's text input.
    """

    widget = forms.Textarea

    def clean(self, value):
        """Returns sanitized text"""
        html = safe_html(value)
        return html


class WYSIWYGField(SafeCharFieldInput):
    """
        Field for displaying a wysiwyg widget.
    """
    widget = WYSIWYGWidget


class MiniWYSIWYGField(WYSIWYGField):
    """
        Field for displaying a wysiwyg widget with only a few tools.
    """
    widget = MiniWYSIWYGWidget
