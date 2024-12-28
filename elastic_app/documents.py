# books/documents.py
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Book

@registry.register_document
class BookDocument(Document):
    class Index:
        name = 'books'  # Elasticsearch index name

    class Django:
        model = Book  # Link the model to this document
        fields = [
            'title',
            'author',
            'description',
            'published_date',
        ]
