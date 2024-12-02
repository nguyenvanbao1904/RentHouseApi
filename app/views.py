from rest_framework import viewsets, generics

from app.models import User
from app.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

