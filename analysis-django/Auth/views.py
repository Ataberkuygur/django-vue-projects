from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class UserViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
    