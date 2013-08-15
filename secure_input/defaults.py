from django.conf import settings


ALLOWED_TAGS = ('a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i',
                'li', 'ol', 'strong', 'ul', 'font', 'div', 'span', 'br',
                'strike', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'table',
                'tr', 'td', 'th', 'thead', 'tbody', 'dl', 'dd', 'u', )

ALLOWED_ATTRIBUTES = {'*': ['class'], 'a': ['href', 'title'],
                      'abbr': ['title'], 'acronym': ['title'],
                      'font': ['face', 'size', ], 'div': ['style', ],
                      'span': ['style', ], 'ul': ['style', ], }

ALLOWED_STYLES = ['font-size', 'color', 'text-align', 'text-decoration',
                  'font-weight', ]

ALLOWED_TAGS = getattr(settings, 'ALLOWED_TAGS', ALLOWED_TAGS)
ALLOWED_ATTRIBUTES = getattr(settings, 'ALLOWED_ATTRIBUTES', ALLOWED_ATTRIBUTES)
ALLOWED_STYLES = getattr(settings, 'ALLOWED_STYLES', ALLOWED_STYLES)

