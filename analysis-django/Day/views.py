from rest_framework.viewsets import ModelViewSet
from .models import Day
from .serializers import DaySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.permissions import IsUserOfObjectOrReadOnly
from .permissions import IsUserOfDayOrReadOnly

class DayViewSet(ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOfDayOrReadOnly]
    lookup_field = 'slug'
