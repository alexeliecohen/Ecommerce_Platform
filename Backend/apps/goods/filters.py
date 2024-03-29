import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    Goods Filter
    """
    pricemin = django_filters.NumberFilter(field_name='shop_price', help_text="Min Price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price', help_text="Max Price", lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin','seller', 'pricemax', 'is_hot', 'is_new']
