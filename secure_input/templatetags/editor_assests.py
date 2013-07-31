from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('secure_input/tags/requirements.html')
def all_editor_assets():
    return {"STATIC_URL": settings.STATIC_URL}


@register.inclusion_tag('secure_input/tags/css.html')
def css_editor_assets(include_bootstrap=True):
    return {"STATIC_URL": settings.STATIC_URL, 'bootstrap': include_bootstrap}


@register.inclusion_tag('secure_input/tags/js.html')
def js_editor_assets(include_bootstrap=True, include_hotkeys=True):
    return {"STATIC_URL": settings.STATIC_URL, 'bootstrap': include_bootstrap,
            'hotkeys': include_hotkeys}
