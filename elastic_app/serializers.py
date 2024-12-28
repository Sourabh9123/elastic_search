# books/serializers.py
from rest_framework import serializers

class BookDocumentSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    published_date = serializers.DateTimeField()

    
