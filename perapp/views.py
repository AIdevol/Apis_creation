from rest_framework import viewsets, permissions
from .models import User, Permission, Group
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer
# Create your views here.

class UserViewSets(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class PermissionViewSets(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class GroupViewSets(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class = GroupSerializer