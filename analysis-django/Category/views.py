from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.permissions import IsUserOfObjectOrReadOnly

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOfObjectOrReadOnly]
    lookup_field = 'id'

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)
