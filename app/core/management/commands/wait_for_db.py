
# for sleeping interface
import time

# pause if database connection is available
from django.db import connections
# if DB isn't available throw error
from django.db.utils import OperationalError
# if we would like to create custom command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until DB is available"""

    def handle(self, *args, **options):

        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second....')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available!'))


