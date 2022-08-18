from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            User.objects.create_superuser('admin', 'admin@example.com', 'pass')
        except:
            print('Error while creating Admin account!')

