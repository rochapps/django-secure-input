"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django import forms
from django.test import TestCase

from .fields import SafeCharFieldInput
from .widgets import WYSIWYGWidget


class ExampleForm(forms.Form):
    text = SafeCharFieldInput()


class ExampleWYSIWYGForm(forms.Form):
    text = SafeCharFieldInput(widget=WYSIWYGWidget)


class SecureTextInputTests(TestCase):

    def setUp(self):
        self.form = ExampleForm

    @property
    def malicious_text(self):
        text = "<script>alert('I am taking over your browser')</script>"
        return text

    @property
    def almost_clean_text(self):
        text = "<p><a href='/bad/'>This tag</a> is valid.</p><aside>This one is not.</aside>"
        return text

    @property
    def clean_text(self):
        text = "<h2>This is a nice person</h2><h2>Using safe markup when you " \
               "posting in the internet is important</h2><p>When you play nice" \
               "you make the internet more safe for everyone and make" \
               "programmers lives easier"
        return text

    def test_malicious_text(self):
        """Form will validate but the malicious input will be sanitized.
        Script tags are not allowed.
        """
        data = {'text': self.malicious_text}
        form = self.form(data)
        self.failUnless(form.is_valid())
        cleaned_text = form.cleaned_data['text']
        escaped_text = u"alert('I am taking over your browser')"
        self.assertEqual(cleaned_text, escaped_text)

    def test_almost_clean_text(self):
        data = {'text': self.almost_clean_text}
        form = self.form(data)
        self.failUnless(form.is_valid())
        cleaned_text = form.cleaned_data['text']
        escaped_text_v1 = u'<p><a rel="nofollow" href="/bad/">This tag</a> is valid.</p>' \
                          u"This one is not."
        escaped_text_v2 = u'<p><a href="/bad/" rel="nofollow">This tag</a> is valid.</p>' \
                          u"This one is not."
        self.assert_(cleaned_text == escaped_text_v1 or cleaned_text == escaped_text_v2)

    def test_clean_text(self):
        text = self.clean_text
        data = {'text': text}
        form = self.form(data)
        self.failUnless(form.is_valid())
        cleaned_text = form.cleaned_data['text']
        escaped_text = text + '</p>'  # Bleach closes unclosed tags.
        self.assertEqual(cleaned_text, escaped_text)


class WYSIWYGWidgetTest(TestCase):

    def setUp(self):
        self.form = ExampleWYSIWYGForm()

    def test_render(self):
        pass
