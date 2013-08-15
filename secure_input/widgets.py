from django import forms
from django.template.loader import render_to_string

__all__ = ('WYSIWYGWidget', )


class WYSIWYGWidget(forms.Textarea):
    """Custom bootstrap-wysiwyg widget."""
    template_name = 'secure_input/widgets/full_wysiwyg.html'

    def render(self, name, value, attrs=None):
        """Include a hidden input to stored the serialized upload value."""
        context = attrs or {}
        context.update({'name': name, 'value': value, })
        return render_to_string(self.template_name, context)

    class Media:
        css = {
            'all': (
                'secure_input/bootstrap/css/bootstrap.css',
                'secure_input/font-awesome/css/font-awesome.css',
                'secure_input/css/basicEditor.css',
            )
        }
        js = (
            'secure_input/js/libs/jquery.js',
            'secure_input/bootstrap/js/bootstrap.js',
            'secure_input/bootstrap-wysiwyg/external/jquery.hotkeys.js',
            'secure_input/bootstrap-wysiwyg/bootstrap-wysiwyg.js',
            'secure_input/js/plugin.js',
        )


class MiniWYSIWYGWidget(WYSIWYGWidget):
    """Renders a bootstrap-wysiwyg widget with very few tools."""
    template_name = 'secure_input/widgets/mini_wysiwyg.html'