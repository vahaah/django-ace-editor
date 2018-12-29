# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django import forms
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe


class AceWidget(forms.Textarea):
	def __init__(self, mode=None, theme=None, wordwrap=False, width="500px", height="300px", showprintmargin=True,
	             *args, **kwargs):
		self.mode = mode
		self.theme = theme
		self.wordwrap = wordwrap
		self.width = width
		self.height = height
		self.showprintmargin = showprintmargin
		super(AceWidget, self).__init__(*args, **kwargs)
	
	@property
	def media(self):
		js = [
			"djace_editor/ace/ace.js",
			"djace_editor/widget.js",
		]
		if self.mode:
			js.append("djace_editor/ace/mode-%s.js" % self.mode)
		if self.theme:
			js.append("djace_editor/ace/theme-%s.js" % self.theme)
		css = {
			"screen": ["djace_editor/widget.css"],
		}
		return forms.Media(js=js, css=css)
	
	def render(self, name, value, attrs=None, renderer=None):
		attrs = attrs or {}
		
		ace_attrs = {
			"class": "django-ace-widget loading",
			"style": "width:%s; height:%s" % (self.width, self.height)
		}
		toolbar_modes = getattr(settings, 'DJACE_TOLBAR_MODES', {})
		if self.mode:
			ace_attrs["data-mode"] = self.mode
			if self.mode not in toolbar_modes:
				toolbar_modes[self.mode] = self.mode
		if self.theme:
			ace_attrs["data-theme"] = self.theme
		if self.wordwrap:
			ace_attrs["data-wordwrap"] = "true"
		ace_attrs["data-showprintmargin"] = "true" if self.showprintmargin else "false"
		
		textarea = super(AceWidget, self).render(name, value, attrs, renderer)
		
		html = '<div%s><div></div></div>%s' % (flatatt(ace_attrs), textarea)
		toolbar_mode_options = ''
		for k, v in toolbar_modes.items():
			toolbar_mode_options += '<option value="%s">%s</option>' % (k, v)
		
		# add toolbar
		html = '<div class="django-ace-editor">' \
		       '<div style="width: %s" class="django-ace-toolbar">' \
				'<select class="django-ace-mode_select">%s</select>' \
		       '<a href="./" class="django-ace-max_min"></a>' \
		       '</div>%s</div>' % (
			self.width, toolbar_mode_options, html)
		
		return mark_safe(html)
