#!/usr/bin/env python
import sys

import django

from django.conf import settings


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=(
            'secure_input',
        ),
        SITE_ID=1,
        SECRET_KEY='this-is-just-for-tests-so-not-that-secret',
    )


from django.test.utils import get_runner


def runtests():
    if django.VERSION >= (1,7,0):
        django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['secure_input', ])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()

