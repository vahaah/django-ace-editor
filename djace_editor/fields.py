# -*- coding: utf-8 -*-
from django.db.models import Field
from django.conf import settings

from .widgets import AceWidget


class AceField(Field):
    def __init__(self, *args, **kwargs):
        mode = kwargs.pop('mode', None)
        theme = kwargs.pop('theme', None)
        wordwrap = kwargs.pop('wordwrap', False)
        width = kwargs.pop('width', u"500px")
        height = kwargs.pop('height', u"300px")
        showprintmargin = kwargs.pop('showprintmargin', True)
        self.widget = AceWidget(
            mode=mode,
            theme=theme,
            wordwrap=wordwrap,
            width=width,
            height=height,
            showprintmargin=showprintmargin
        )
        super(AceField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)
        return super(AceField, self).formfield(**defaults)