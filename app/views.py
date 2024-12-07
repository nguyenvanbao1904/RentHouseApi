from rest_framework import viewsets, generics
from rest_framework.viewsets import ViewSet
from django.shortcuts import render

from app.models import User
from app.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def LoginView(request):
    return render(request, 'login.html')

