secure_input
========================

Let your users input html into your textareas without losing any sleep.
django-secure-input sanitizes user's input and allows only some tags to be
interpreted as html and escapes the rest. By default, <script> tags are not allowed.

.. image::
    https://secure.travis-ci.org/rochapps/django-secure-input.png?branch=master
    :alt: Build Status
        :target: https://secure.travis-ci.org/rochapps/django-secure-input

Requirements/Installing
-----------------------------------

django-secure-input requires Python 2.6-2.7 or 3.2+. It also requires Django >= 1.4
and bleach.

The easiest way to install django-secure-input is using `pip <http://www.pip-installer.org/>`_::

    pip install django-secure-input


The add it to your install apps::

    INSTALLED_APP += ('secure_input')


Fields
-----------------------------------

Use one of our provided custom form fields in your forms and you are all set.

    **SafeCharFieldInput**
        Textarea that allows saving html.

    **WYSIWYGField**
        wysiwyg widget

    **MiniWYSIWYGField**
        wysiwyg widget (limiited tools)




Defaults settings
-----------------------------------

The defaults provided
by our validation method can be overwritten, to set your own overwrite this on
your settings.py file:

    **ALLOWED_TAGS**:       Tuple of allowed tags, for example: ('p', 'h2', 'h3').

    **ALLOWED_STYLES**:     Tuple of inline style allowable in your html, for
                          example: ('font', 'font-size', 'color').

    **ALLOWED_ATTRIBUTES**: A dict of tags -> attributes, for example:
                          {'a': ['href', 'title'], '*': ['class']}


Example
-----------------------------------
Simplest way to start using our custom fields::

    from django import forms
    from secure_input.fields import MiniWYSIWYGField

    class MySecureForm(forms.ModelForm):
        text = MiniWYSIWYGField()

        class Meta:
            model = MyModel


Template
-------------------------------------
Make sure to include the following css and js files in the template where you
are rendering your form.

In your template {{ form.media.css }}::

- <link href="{{ STATIC_URL }}secure_input/bootstrap/css/bootstrap.css" rel="stylesheet" type="css/text">
- <link href="{{ STATIC_URL }}secure_input/font-awesome/css/font-awesome.css" rel="stylesheet" type="css/text">
- <link href="{{ STATIC_URL }}secure_input/css/basicEditor.css" rel="stylesheet" type="css/text">

and {{form.media.js }}::

- <script src="{{ STATIC_URL }}secure_input/js/libs/jquery.js" type="text/javascript"></script>
- <script src="{{ STATIC_URL }}secure_input/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
- <script src="{{ STATIC_URL }}secure_input/bootstrap-wysiwyg/external/jquery.hotkeys.js" type="text/javascript"></script>
- <script src="{{ STATIC_URL }}secure_input/bootstrap-wysiwyg/bootstrap-wysiwyg.js" type="text/javascript"></script>
- <script src="{{ STATIC_URL }}secure_input/js/plugin.js" type="text/javascript"></script>

Finally, you need to initialize the js plugin::

    $("#commentForm").secureInput();


Documentation
-----------------------------------

Additional documentation on using django-secure-input is available on
`Read The Docs <http://readthedocs.org/docs/django-secure-input/>`_.


Running the Tests
------------------------------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py


License
--------------------------------------

django-secure-input is released under the BSD License. See the
`LICENSE <https://github.com/rochapps/django-secure-input/blob/master/LICENSE>`_ file for more details.


Contributing
--------------------------------------

If you think you've found a bug or are interested in contributing to this project
check out `django-secure-input on Github <https://github.com/rochapps/django-secure-input>`_.

Development sponsored by `RochApps, LLC
<http://www.rochapps.com/services>`_.