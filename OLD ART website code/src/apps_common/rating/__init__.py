"""
    Модуль голосования для составления рейтинга сайта (для schema.org).

    Установка:
        settings.py:
            INSTALLED_APPS = (
                ...
                'rating',
                ...
            )

            SUIT_CONFIG = (
                ...
                {
                    'app': 'rating',
                    'icon': 'icon-lock',
                    'models': (
                        'RatingVote',
                    )
                },
                ...
            )

"""

default_app_config = 'rating.apps.Config'
