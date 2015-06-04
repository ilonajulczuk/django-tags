import django_filters

from .models import Library, Tag


class LibraryFilter(django_filters.FilterSet):
    # default for CharFilter is to have exact lookup_type
    name = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')

    # tricky part - how to filter by related field?
    # but not by its foreign key (default)
    # `to_field_name` is crucial here
    # `conjoined=True` makes that, the more tags, the more narrow the search
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        to_field_name='text',
        conjoined=True,
    )

    class Meta:
        model = Library
        fields = ['name', 'description', 'tags']
