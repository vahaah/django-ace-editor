Ace editor for Django
=====================

What's that
-----------

*djace_editor* is a reusable application for Django, using `Ace editor <http://ace.c9.io/>`_

Forked on `Bradley Ayers <https://github.com/bradleyayers/django-ace/>`_.

Dependence
----------

- `Django >= 1.9`

Getting started
---------------

- Install *djace_editor*:

```pip install djace_editor```

- Add `'djace_editor'` to INSTALLED_APPS.


Using in model
--------------

.. code-block:: python

    from django.db import models
    from djace_editor import AceField

    class Entry(models.Model):
        title = models.CharField(max_length=250, verbose_name=u'Title')
        text = AceField(verbose_name=u'Text')

or use custom parametrs:

.. code-block:: python

    text = AceField(
        verbose_name=u'Text',
        theme="terminal",
        width="800px",
        height="500px"
    )

Using for only admin interface
------------------------------

.. code-block:: python

    from django import forms
    from djace_editor import AceWidget
    from blog.models import Entry

    class EntryAdminForm(forms.ModelForm):
        class Meta:
            model = Entry
            widgets = {
               'short_text': AceWidget(),
            }

    class EntryAdmin(admin.ModelAdmin):
        form = EntryAdminForm

`AceWidget` takes the same parameters as `AceField`.



Contributing
------------

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request =]