from rest_framework import filters, viewsets

from .filters import LibraryFilter
from .models import Library, Tag
from .serializers import LibrarySerializer, TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = LibraryFilter
