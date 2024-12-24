from django.conf import settings

ADMIN_MAP_WIDTH = getattr(settings, 'GOOGLE_MAP_ADMIN_WIDTH', '')
ADMIN_MAP_HEIGHT = getattr(settings, 'GOOGLE_MAP_ADMIN_HEIGHT', 300)
ADMIN_MAP_ZOOM = getattr(settings, 'GOOGLE_MAP_ADMIN_ZOOM', 16)

STATIC_MAP_URL = 'https://maps.googleapis.com/maps/api/staticmap?key=' + getattr(settings, 'GOOGLE_MAPS_API_KEY', '')
STATIC_MAP_WIDTH = getattr(settings, 'GOOGLE_MAP_STATIC_WIDTH', 300)
STATIC_MAP_HEIGHT = getattr(settings, 'GOOGLE_MAP_STATIC_HEIGHT', 200)
STATIC_MAP_ZOOM = getattr(settings, 'GOOGLE_MAP_STATIC_ZOOM', 14)

EXTERNAL_MAP_URL = 'https://maps.google.com/maps?'

GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/xml?key=' + getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

# Default coordinates returned when actual coordinates cannot be determined
DEFAULT_MAP_CENTER = (49.418785, 53.510171)
