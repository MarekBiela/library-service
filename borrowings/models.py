from django.db import models
from django.db.models import ForeignKey
from django.core.exceptions import ValidationError

from books.models import Book
from users.models import User


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    book = ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def clean(self):
        if self.expected_return_date < self.borrow_date:
            raise ValidationError("Expected return date cannot be before borrow date.")

        if self.return_date and self.return_date < self.borrow_date:
            raise ValidationError("Return date cannot be before borrow date.")