import os
import sys

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'testapp.settings'


def runtests():
    from django.test.utils import get_runner
    from django.conf import settings

    if hasattr(django, 'setup'):
        django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['testapp'])
    sys.exit(bool(failures))
