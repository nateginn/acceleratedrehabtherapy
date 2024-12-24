from django.conf import settings

EXCLUDE_DIRS = getattr(settings, 'BACKUP_EXCLUDE_DIRS', [])
EXCLUDE_MODELS = getattr(settings, 'BACKUP_EXCLUDE_MODELS', [])
