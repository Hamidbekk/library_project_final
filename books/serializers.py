from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it contains numbers
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Iltimos kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak"
                }
            )

        # check title and author from database existance
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "This book has been already added to the database"
                }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 2000:
            raise ValidationError(
                {
                    "status": False,
                    "message": "This price is not possible"
                }
            )


