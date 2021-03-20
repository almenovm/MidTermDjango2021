from rest_framework import viewsets
from main.models import *
from main.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]


class JournalViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
