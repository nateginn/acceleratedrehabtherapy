from django import forms
from django.utils.html import smart_urlquote


class TokenButtonWidget(forms.Widget):
    template_name = 'social_networks/token_button_widget.html'

    def __init__(self, text='', attrs=None):
        super().__init__(attrs=attrs)
        self.text = str(text)
        self.attrs.setdefault('target', '_self')
        self.attrs.setdefault('class', 'btn btn-info')

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if value:
            href = smart_urlquote(value)
            context.update({
                'href': href,
                'text': self.text or href
            })
        return context
