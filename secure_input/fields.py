import bleach
from django import forms
from django.conf import settings

ALLOWED_TAGS = ('a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i',
                'li', 'ol', 'strong', 'ul', 'font', 'div', 'span', 'br',
                'strike', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'table',
                'tr', 'td', 'th', 'thead', 'tbody', 'dl', 'dd', )

ALLOWED_ATTRIBUTES = {'*': ['class'], 'a': ['href', 'title'],
                      'abbr': ['title'], 'acronym': ['title'],
                      'font': ['face', 'size',], 'div': ['style', ],
                      'span': ['style', ], 'ul': ['style', ], }

ALLOWED_STYLES = ['font-size', 'color', 'text-align', 'text-decoration',
                  'font-weight', ]


class SecureCharFieldInput(forms.CharField):
    """Widget that provides custom clean method to sanitize user's text input.
    """

    widget = forms.TextInput

    def clean(self, value):
        """Returns sanitized text"""
        tags = getattr(settings, 'ALLOWED_TAGS', ALLOWED_TAGS)
        attributes = getattr(settings, 'ALLOWED_ATTRIBUTES', ALLOWED_ATTRIBUTES)
        styles = getattr(settings, 'ALLOWED_STYLES', ALLOWED_STYLES)
        cleaned_value = bleach.clean(value, tags=tags, attributes=attributes,
                                     styles=styles)
        return cleaned_value
