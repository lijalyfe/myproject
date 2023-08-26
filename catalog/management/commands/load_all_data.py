from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Clear old data and load fixtures for categories and products'

    def handle(self, *args, **options):
        # Delete old categories and products
        Category.objects.all().delete()
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted old data'))

        # Load fixtures
        categories_fixture_file = 'categories_fixture.json'
        products_fixture_file = 'products_fixture.json'
        call_command('loaddata', categories_fixture_file)
        call_command('loaddata', products_fixture_file)
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded fixtures from {categories_fixture_file} and {products_fixture_file}'))
