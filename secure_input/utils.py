import bleach

from .defaults import ALLOWED_ATTRIBUTES, ALLOWED_TAGS, ALLOWED_STYLES, STRIP_TAGS


def safe_html(html):
    html = html or ''
    linkified_html = bleach.linkify(html)
    cleaned_html = bleach.clean(linkified_html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
                                styles=ALLOWED_STYLES, strip=STRIP_TAGS)
    return cleaned_html
