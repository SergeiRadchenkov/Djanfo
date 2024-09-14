from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello world!' to outpur."

    def handle(self, *args, **options):
        self.stdout.write('Hello, world!')
