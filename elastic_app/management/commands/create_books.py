import random
from django.core.management.base import BaseCommand
from faker import Faker
from elastic_app.models import Book
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Generate dummy data for the Book model"

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of dummy books to create')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']
        books = []

        for _ in range(count):
            title = fake.catch_phrase()
            author = fake.name()
            description = fake.text(max_nb_chars=500)
           
            books.append(Book(
                title=title,
                author=author,
                description=description,
                
            ))

        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS(f"Successfully created {count} dummy books!"))


## python manage.py create_books --count 50 
## default is 10 count
