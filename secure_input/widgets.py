from __future__ import unicode_literals

from django import forms
from django.forms.util import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe

__all__ = ('WYSIWYGWidget', )


class WYSIWYGWidget(forms.Textarea):
    """Custom bootstrap-wysiwyg widget."""

    def render(self, name, value, attrs=None):
        """Include a hidden input to stored the serialized upload value."""
        attrs = attrs or {}
        editor_id = "{name}-secure-input".format(name=name)
        attrs.update({'data-editor': editor_id, 'class': 'hidden secure-input'})
        textarea = super(WYSIWYGWidget, self).render(name, value, attrs=attrs)
        editor_attrs = {"class": "bootstrap-wysiwyg", 'id': editor_id}
        editor = format_html('<div{0} /></div>', flatatt(editor_attrs))
        return mark_safe(textarea + editor)