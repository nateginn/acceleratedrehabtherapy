from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        permissions = (
            ('admin_menu', 'Can see hidden menu items'),
        )
