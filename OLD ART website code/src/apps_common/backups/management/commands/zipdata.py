import os
import zipfile
from datetime import datetime
from django.conf import settings
from django.core.management import BaseCommand, call_command, CommandError
from ... import conf


class Command(BaseCommand):
    """
        Создание дампа данных в zip-архиве
    """
    args = '<output directory>'
    help = 'Creates ZIP-archive with media and database dump'

    def handle(self, *args, **options):
        date = datetime.now().date()

        backup_name = '{}.zip'.format(date.strftime('%Y_%m_%d'))
        if args:
            backup_dir = os.path.abspath(args[0])
        else:
            backup_dir = settings.BACKUP_ROOT

        if not os.path.exists(backup_dir):
            raise CommandError('output directory does not exists')

        backup_path = os.path.join(backup_dir, backup_name)
        backup_excludes = [
            os.path.normpath(os.path.join(settings.MEDIA_ROOT, d))
            for d in conf.EXCLUDE_DIRS
        ]

        with zipfile.ZipFile(backup_path, 'w') as ziph:
            for root, dirs, files in os.walk(settings.MEDIA_ROOT, topdown=True):
                dirs[:] = [
                    d for d in dirs
                    if os.path.normpath(os.path.join(root, d)) not in backup_excludes
                ]

                for file in files:
                    abspath = os.path.abspath(os.path.join(root, file))
                    relpath = os.path.relpath(abspath, settings.MEDIA_ROOT)
                    ziph.write(abspath, os.path.join('media', relpath))

            # DB dump
            dump_path = os.path.join(settings.BASE_DIR, 'dump.json')
            call_command('dump', output=dump_path, exclude=conf.EXCLUDE_MODELS)
            ziph.write(dump_path, 'dump.json')

        os.unlink('dump.json')
        self.stdout.write('backup saved to "%s"' % backup_path)
