from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrAuthenticated


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrAuthenticated]
