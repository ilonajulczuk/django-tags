from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from tags.models import Library
from tags.serializers import LibrarySerializer


class LibraryViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
