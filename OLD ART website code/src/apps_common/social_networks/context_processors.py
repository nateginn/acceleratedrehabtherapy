from .models import SocialConfig


def google_apikey(request):
    config = SocialConfig.get_solo()
    return {
        'GOOGLE_MAPS_API_KEY': config.google_apikey,
    }
