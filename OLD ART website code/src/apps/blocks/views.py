from django.template import loader

from blocks.models import Advantages, Focuses, Partners
from blog.models import BlogPost
from contacts.models import Address
from services.models import Service


def location_block_render(context, block, **kwargs):
    return loader.render_to_string('blocks/location.html', {
        'block': block,
    }, request=context.get('request'))


def our_team_block_render(context, block, **kwargs):
    return loader.render_to_string('blocks/our_team.html', {
        'block': block,
    }, request=context.get('request'))


def insurances_block_render(context, block, **kwargs):
    return loader.render_to_string('blocks/insurances.html', {
        'block': block,
    }, request=context.get('request'))


def appointment_block_render(context, block, **kwargs):
    return loader.render_to_string('blocks/appointment.html', {
        'block': block,
    }, request=context.get('request'))


def share_block_render(context, block, **kwargs):
    return loader.render_to_string('blocks/share.html', {
        'block': block,
    }, request=context.get('request'))


def why_block_render(context, block, **kwargs):
    advantages = Advantages.objects.all()
    
    if not advantages:
        return ''
    
    return loader.render_to_string('blocks/why_choose_us.html', {
        'block': block,
    }, request=context.get('request'))


def focus_on_block_render(context, block, **kwargs):
    focuses = Focuses.objects.all()
    
    if not focuses:
        return ''
    
    return loader.render_to_string('blocks/focus_on.html', {
        'block': block,
    }, request=context.get('request'))


def our_mission_block_render(context, block, **kwargs):
    return loader.render_to_string('blocks/our_mission.html', {
        'block': block,
    }, request=context.get('request'))


def partners_block_render(context, block, **kwargs):
    partners = Partners.objects.all()
    
    if not partners:
        return ''
    
    return loader.render_to_string('blocks/partners.html', {
        'block': block,
    }, request=context.get('request'))


def blog_block_render(context, block, **kwargs):
    posts = BlogPost.objects.visible()
    config = context.get('config')
    
    if not posts:
        return ''
    
    if config:
        if isinstance(config, BlogPost):
            posts = posts.exclude(pk=config.pk)
    
    return loader.render_to_string('blocks/blog.html', {
        'block': block,
        'posts': posts,
    }, request=context.get('request'))


def service_block_render(context, block, **kwargs):
    services = Service.objects.root_nodes().filter(visible=True)
    
    if not services:
        return ''
    
    return loader.render_to_string('blocks/services.html', {
        'block': block,
        'services': services
    }, request=context.get('request'))


def contact_block_render(context, block, **kwargs):
    return loader.render_to_string('blocks/contacts.html', {
        'addresses': Address.objects.all(),
        'block': block,
    }, request=context.get('request'))
