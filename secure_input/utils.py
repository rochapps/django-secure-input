import bleach

from .defaults import ALLOWED_ATTRIBUTES, ALLOWED_TAGS, ALLOWED_STYLES, STRIP_TAGS


def safe_html(html):
    html = html or ''
    cleaned_html = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
                                styles=ALLOWED_STYLES, strip=STRIP_TAGS)
    return bleach.linkify(cleaned_html)
