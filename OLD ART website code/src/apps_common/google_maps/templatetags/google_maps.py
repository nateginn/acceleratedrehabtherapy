from libs import jinja2
from ..api import get_static_map_url, get_external_map_url
from ..models import geocode_cached


@jinja2.extension
class GoogleMapsExtension(jinja2.Extension):
    tags = {'google_map_static', 'google_map_external'}

    def _google_map_static(self, address, zoom=None, width=None, height=None):
        """
            Returns the URL of an image with a map.
            Can be applied to a MapAndAddress class object, an address string,
            or a GoogleCoords instance.

            Parameters:
                zoom level, width, height - comma separated.

            Example:
                <img src="{% google_map_static address zoom=15 width=300 height=200 %}">
        """
        if not address:
            return ''

        lng, lat = geocode_cached(address)
        return get_static_map_url(lng, lat, zoom=zoom, width=width, height=height)

    def _google_map_external(self, address, zoom=14):
        """
            Returns the URL of the map in Google Maps service.
            Can be applied to a MapAndAddress class object, an address string,
            or a GoogleCoords instance.

            Takes an optional parameter: zoom level.

            Example:
                <a href="{% google_map_external address zoom=15 %}" target="_blank">Show Map</a>
        """
        if not address:
            return ''

        lng, lat = geocode_cached(address)
        return get_external_map_url(lng, lat, zoom)
