from django.template import loader
from libs import jinja2


@jinja2.extension
class MenuExtension(jinja2.Extension):
    tags = {'menu'}
    takes_context = True

    def _menu(self, context, name, template='menu/menu.html'):
        request = context.get('request')
        if not request:
            return ''

        menus = getattr(request, '_menus', None)
        if not menus:
            return ''

        return loader.render_to_string(template, {
            'level': 1,
            'items': menus.get(name, ()),
        }, request=context.get('request'))
