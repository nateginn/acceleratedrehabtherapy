from django.template import loader

from .models import Testimonial


def block_render(context, block, **kwargs):
    request = context.get('request')
    
    if not request:
        return ''
    
    testimonials = Testimonial.objects.filter(visible=True)
    
    if not testimonials:
        return ''
    
    return loader.render_to_string('testimonials/block.html', {
        'block': block,
        'testimonials': testimonials,
    }, request=context.get('request'))
