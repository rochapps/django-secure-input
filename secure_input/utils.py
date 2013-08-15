import bleach

from .defaults import ALLOWED_ATTRIBUTES, ALLOWED_TAGS, ALLOWED_STYLES


def safe_html(html):
    html = html or ''
    cleaned_html = bleach.clean(html, tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRIBUTES, styles=ALLOWED_STYLES)
    return cleaned_html