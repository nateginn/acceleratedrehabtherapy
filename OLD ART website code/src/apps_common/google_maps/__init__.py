"""
    Depends on:
        social_networks
        libs.coords

    Required to include:
        google_maps/js/core.js

    Installation:
        settings.py:
            INSTALLED_APPS = (
                ...
                'google_maps',
                ...
            )

            TEMPLATES = [
                {
                    ...
                    'OPTIONS': {
                        'context_processors': (
                            ...
                            'social_networks.context_processors.google_apikey',
                        ),
                    }
                },
            ]

    Settings (settings.py):
        GOOGLE_MAP_ADMIN_WIDTH - map width in admin (default 100%)
        GOOGLE_MAP_ADMIN_HEIGHT - map height in admin (default 300px)
        GOOGLE_MAP_ADMIN_ZOOM - map zoom in admin (default 16)

        GOOGLE_MAP_STATIC_WIDTH - static map width (default 300px)
        GOOGLE_MAP_STATIC_HEIGHT - static map height (default 200px)
        GOOGLE_MAP_STATIC_ZOOM - static map zoom (default 14)

    Examples:
        script.py:
            from google_maps.api import geocode
            from google_maps.models import geocode_cached

            # Get coordinates by address.
            lng, lat = geocode('Togliatti, Mira 35', timeout=0.5)

            # Get coordinates by address with caching results
            lng, lat = geocode_cached('Togliatti, Mira 35', timeout=0.5)

        models.py:
            from google_maps.fields import GoogleCoordsField
            ...

            address = models.CharField(_('address'), max_length=255, blank=True)
            coords = GoogleCoordsField(_('coordinates'), null=True, blank=True)

        page.js:
            $(document).ready(function() {
                var gmap = GMap('#gmap', {
                    zoom:13
                }).on('ready', function() {
                    var marker = GMapMarker({
                        map: this,
                        position: GMapPoint(53.510171, 49.418785),
                        hint: 'First',
                        balloon: '<p>Hello</p>'
                    })
                });
            });

        Admin Javascript:
            // Get coordinates by address in another field
            $(document).on('change', '#id_address', function() {
                var gmap = $('#id_coords').next('.google-map').data('gmap');
                gmap.geocode($(this).val(), function(point) {
                    var marker = this.markers[0];
                    if (marker) {
                        marker.position(point);
                    } else {
                        marker = GMapMarker({
                            map: this,
                            position: point
                        })
                    }

                    marker.trigger('dragend');
                    this.panTo(point);
                });
            });

        template.html:
            <!-- Static map with zoom level 15 size 300x200 -->
            <img src="{% google_map_static address zoom=15 width=300 height=200 %}">

            <!-- Link to map in Google service -->
            <a href="{% google_map_external address zoom=15 %}" target="_blank">Show Map</a>
"""

default_app_config = 'google_maps.apps.Config'