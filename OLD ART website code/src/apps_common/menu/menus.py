from django.utils.translation import ugettext_lazy as _

from services.models import Service
from .base import Menu, MenuItem

services = Service.objects.root_nodes().filter(visible=True)
sub_services = Service.objects.filter(important_in_menu=True, visible=True)


def main(request):
    menu = Menu()
    
    for service in sub_services:
        if service.visible and service.important_in_menu:
            menu.append(
                MenuItem(
                    attrs={'class': 'service_left_menu'},
                    item_id='services',
                    title=service.title,
                    url=service.get_absolute_url(),
                )
            )
    
    for service in services:
        if service.visible:
            menu.append(
                MenuItem(
                    attrs={'class': 'root_service'},
                    title=service.title,
                    url=service.get_absolute_url(),
                )
            )
    
    menu.append(
        MenuItem(
            title=_('Services'),
            url='main:index',
            attrs={'class': 'menu-services'},
        ),
        MenuItem(
            title=_('About'),
            url='about:index',
        ),
        MenuItem(
            title=_('Blog'),
            url='blog:index',
        ),
        MenuItem(
            title=_('Contact'),
            url='contacts:index',
        ),
    )
    return menu
