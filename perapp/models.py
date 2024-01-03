# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from mptt.models import MPTTModel, TreeForeignKey

# class User(AbstractUser):
#     groups = models.ManyToManyField('Group', blank=True)
#     permissions = models.ManyToManyField('Permission', blank=True, related_name='user_permissions_custom')

# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     permissions = models.ManyToManyField('Permission', through='GroupPermission')

# class Permission(MPTTModel):
#     name = models.CharField(max_length=100)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

# class GroupPermission(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('group', 'permission')
from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class User(AbstractUser):
    pass

class Group(models.Model):
    name=models.CharField(max_length=100)

class Permission(MPTTModel):
    name = models.CharField(max_length=100)
    parents = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

class GroupPermission(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group','permission')