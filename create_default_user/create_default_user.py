import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Create a default superuser if it does not exist'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            help='Specify the username of the default superuser (overrides environment variables)'
        )
        parser.add_argument(
            '--password',
            type=str,
            help='Specify the password of the default superuser (overrides environment variables)'
        )
        parser.add_argument(
            '--email',
            type=str,
            help='Specify the email of the default superuser (overrides environment variables)'
        )

    def handle(self, *args, **options):
        # Fetching from shortened environment variables
        username = options.get('username') or os.getenv('SU_NAME', 'admin')
        password = options.get('password') or os.getenv('SU_PASS', 'admin')
        email = options.get('email') or os.getenv('SU_EMAIL', 'admin@example.com')

        User = get_user_model()

        if not User.objects.filter(username=username).exists():
            try:
                User.objects.create_superuser(
                    username=username,
                    password=password,
                    email=email,
                )
                self.stdout.write(self.style.SUCCESS(f'Default superuser "{username}" created successfully.'))
            except IntegrityError as e:
                raise CommandError(f'Failed to create superuser: {str(e)}')
            except Exception as e:
                raise CommandError(f'An unexpected error occurred: {str(e)}')
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))
