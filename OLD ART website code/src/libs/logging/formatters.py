import time
import logging
from django.db import connection
from django.utils.log import ServerFormatter
from django.utils.termcolors import colorize


class UTCFormatter(logging.Formatter):
    converter = time.gmtime


class SQLFormatter(ServerFormatter):
    def format(self, record):
        msg = record.msg
        status_code = getattr(record, 'status_code', None)
        if status_code:
            queries = [
                item['sql']
                for item in connection.queries
            ]
            total_queries = len(queries)
            duplicate_queries = len(set(queries))

            msg += ' ' + colorize('(SQL: %s/%s)', fg='yellow', opts=('bold', ))
            record.args += (
                (total_queries - duplicate_queries),
                total_queries
            )

        record.msg = msg
        return super().format(record)
