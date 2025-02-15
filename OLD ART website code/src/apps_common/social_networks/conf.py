from django.utils.translation import ugettext_lazy as _


# ============================================================
#                   Автопостинг
# ============================================================

# Все доступные соцсети для автопостинга
NETWORK_GOOGLE = 'google'
NETWORK_TWITTER = 'twitter'
NETWORK_FACEBOOK = 'facebook'
NETWORK_LINKEDIN = 'linkedin'
ALL_NETWORKS = (
    (NETWORK_FACEBOOK, _('Facebook')),
    (NETWORK_TWITTER, _('Twitter')),
    (NETWORK_GOOGLE, _('Google Plus')),
    (NETWORK_LINKEDIN, _('Linked In')),
)

# Имена соцсетей, доступных для автопостинга на текущем сайте
ALLOWED_NETWORK_NAMES = (
    NETWORK_GOOGLE,
    NETWORK_TWITTER,
    NETWORK_FACEBOOK,
    NETWORK_LINKEDIN,
)

# Часть ALL_NETWORKS, включающая только доступные сети (для choices в модели)
ALLOWED_NETWORKS = tuple(
    pair
    for pair in ALL_NETWORKS
    if pair[0] in ALLOWED_NETWORK_NAMES
)

# Максимальная длина текста для поста
TEXT_MAX_LENGTH = 2048

# Ссылки на соцсети
SOCIAL_LINK_FACEBOOK = 'facebook'
SOCIAL_LINK_TWITTER = 'twitter'
SOCIAL_LINK_PINTEREST = 'pinterest'
SOCIAL_LINK_YOUTUBE = 'youtube'
SOCIAL_LINK_YELP = 'yelp'
SOCIAL_LINK_LINKEDIN = 'linkedin'
SOCIAL_LINK_INSTAGRAM = 'instagram'
SOCIAL_LINK_VIMEO = 'vimeo'
SOCIAL_LINK_CHOICES = (
    (SOCIAL_LINK_FACEBOOK, _('Facebook')),
    (SOCIAL_LINK_INSTAGRAM, _('Instagram')),
    (SOCIAL_LINK_LINKEDIN, _('LinkedIn')),
    (SOCIAL_LINK_TWITTER, _('Twitter')),
    (SOCIAL_LINK_YOUTUBE, _('YouTube')),
)
