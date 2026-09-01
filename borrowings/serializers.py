from rest_framework import serializers

from .models import Borrowing
from books.serializers import BookSerializer


class BorrowingListSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Borrowing
        fields = ["id", "book_title", "borrow_date", "expected_return_date", "return_date"]


class BorrowingDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = [
            "id",
            "borrow_date",
            "expected_return_date",
            "return_date",
            "book"
        ]


