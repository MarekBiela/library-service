from rest_framework import serializers

from .models import Borrowing, Book
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


class BorrowingCreateSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all()
    )

    class Meta:
        model = Borrowing
        fields = ["book", "borrow_date", "expected_return_date"]

    def validate(self, attrs):
        borrowing = Borrowing(
            user=self.context["request"].user,
            **attrs
        )
        borrowing.full_clean()
        return attrs

    def validate_book(self, book):
        if book.inventory < 1:
            raise serializers.ValidationError("Book is unavailable.")
        return book

    def create(self, validated_data):
        user = self.context["request"].user
        book = validated_data["book"]

        book.inventory -= 1
        book.save(update_fields=["inventory"])

        return Borrowing.objects.create(
            user=user,
            **validated_data
        )
