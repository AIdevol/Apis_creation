from rest_framework import serializers
from .models import User, Permission, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        field = '__all__'
    
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        field = '__all__'
    
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        field = '__all__'