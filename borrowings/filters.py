import django_filters

from .models import Borrowing

class BorrowingFilter(django_filters.FilterSet):
    is_active = django_filters.BooleanFilter(
        field_name="return_date",
        lookup_expr="isnull",
    )
    user_id = django_filters.NumberFilter(field_name="user_id")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.request.user.is_staff:
            self.filters.pop("user_id")

    class Meta:
        model = Borrowing
        fields = ["is_active", "user_id"]
