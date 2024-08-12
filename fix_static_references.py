import os
import re
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Replace ../static/ paths with {% static %} in all HTML templates'

    def add_arguments(self, parser):
        parser.add_argument(
            '--directory',
            default=settings.TEMPLATES[0]['DIRS'][0],
            help='The directory to search for HTML files. Defaults to the first template directory.'
        )
        parser.add_argument(
            '--backup',
            action='store_true',
            help='Create a backup of each file before modification.'
        )

    def handle(self, *args, **options):
        template_dir = options['directory']
        create_backup = options['backup']
        print(f"Template directory: {template_dir}")

        if not os.path.isdir(template_dir):
            print(f"The specified directory does not exist: {template_dir}")
            return

        for root, _, files in os.walk(template_dir):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    print(f"Processing file: {file_path}")
                    self.process_file(file_path, create_backup)

    def process_file(self, file_path, create_backup):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except IOError as e:
            print(f"Failed to read file {file_path}: {e}")
            return

        # Print raw content for debugging
        print("Raw content from file:")
        print(content[:500])  # Print the first 500 characters for inspection

        new_content = self.replace_static_paths(content)

        if content != new_content:
            if create_backup:
                backup_path = f"{file_path}.bak"
                try:
                    with open(backup_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Backup created at {backup_path}")
                except IOError as e:
                    print(f"Failed to create backup for {file_path}: {e}")
                    return

            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Successfully updated {file_path}')
            except IOError as e:
                print(f"Failed to write updated content to {file_path}: {e}")
        else:
            print(f'No changes made to {file_path}')

    def replace_static_paths(self, content):
        # Improved regex to match various HTML attributes and handle multi-line cases
        pattern = re.compile(r'(\s+(?:src|href|background|url)\s*=\s*["\'])../static/([^"\']+)(["\'])', re.MULTILINE)

        def replace_func(match):
            # Print the match for debugging
            print(f"Match found: {match.group(0)}")
            return f'{match.group(1)}{{% static \'{match.group(2)}\' %}}{match.group(3)}'

        new_content = pattern.sub(replace_func, content)
        return new_content
