import django_filters
from main.models import Product

class ProductFilters(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Название")
    price_gte = django_filters.NumberFilter(field_name="price", lookup_expr='gte', label="Ценв от")
    price_lte = django_filters.NumberFilter(field_name="price", lookup_expr="lte",label="цена до")

    class Meta:
        model = Product
        fields = ['title', 'price_gte', 'price_lte']