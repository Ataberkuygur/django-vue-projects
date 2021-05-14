from rest_framework.viewsets import ModelViewSet
from .models import Habit
from .serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.permissions import IsUserOfObjectOrReadOnly

class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOfObjectOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)