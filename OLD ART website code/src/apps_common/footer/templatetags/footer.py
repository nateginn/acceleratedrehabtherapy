from django.template import loader

from contacts.models import Address, ContactsConfig
from libs import jinja2
from .. import conf


@jinja2.extension
class FooterExtension(jinja2.Extension):
    tags = {'footer', 'dl_link'}
    takes_context = True
    
    def _footer(self, context, template='footer/footer.html'):
        address = Address.objects.first()
        phone = ''
        hours = ''
        
        if address:
            phone = address.phones[0] if address.phones else ''
            hours = address.hours.all()
        
        return loader.render_to_string(template, {
            'license': ContactsConfig.get_solo().license,
            'address': '%s %s, %s %s' % (
                address.address if address else '',
                address.city if address else '',
                address.region if address else '',
                address.zip if address else '',
            ),
            'hours': hours,
            'phone': phone,
        }, request=context.get('request'))
    
    def _dl_link(self, context, template='footer/dl_link.html'):
        request = context.get('request')
        if not request:
            return ''
        
        rule = conf.RULES.get(request.path_info)
        if rule:
            return loader.render_to_string(template, rule, request=request)
        
        return loader.render_to_string(template, {
            'url': 'https://directlinedev.com/',
            'title': 'Web Development',
            'fallback': True,
        }, request=request)
