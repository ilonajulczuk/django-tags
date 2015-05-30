import django_filters

from .models import Library, Tag


class LibraryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        to_field_name='text',
        conjoined=True,
    )

    class Meta:
        model = Library
        fields = ['name', 'description', 'tags']
