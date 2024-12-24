from django.conf import settings


def cache_key_func(key, key_prefix, version):
    return ':'.join([
        key_prefix,
        settings.SECRET_KEY[:5],
        settings.LANGUAGE_CODE,
        str(version),
        key,
    ])


def reverse_key_func(key):
    return key.split(':')[-1]
