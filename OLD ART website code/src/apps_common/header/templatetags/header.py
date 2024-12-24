from django.template import loader

from contacts.models import Address
from libs import jinja2


@jinja2.extension
class HeaderExtension(jinja2.Extension):
    tags = {'header'}
    takes_context = True
    
    def _header(self, context, template='header/header.html'):
        address = Address.objects.first()
        phone = ''
        hours = ''
        
        if address:
            phone = address.phones[0] if address.phones else ''
            hours = address.hours.all()
        
        return loader.render_to_string(template, {
            'is_main_page': context.get('is_main_page'),
            'addresses': Address.objects.all(),
            'phone': phone,
            'hours': hours,
        }, request=context.get('request'))
