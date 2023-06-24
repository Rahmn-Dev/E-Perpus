import csv
from django.core.management.base import BaseCommand
from app.models import buku

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app/data/books.csv', type=str)

    def handle(self, *args, **options):
        csv_file = options['app/data/books.csv']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                buku.objects.create(
                    kode_buku=row['kode_buku'],
                    judul_buku=row['judul_buku'],
                    pengarang=row['pengarang'],
                    genre=row['genre'],
                )
        self.stdout.write(self.style.SUCCESS('CSV import completed successfully'))