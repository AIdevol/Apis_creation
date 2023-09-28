from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Service(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    BODY_LOCATIONS=(
        ('head', 'Head'),
        ('neck', 'Neck'),
        ('arm', 'Arm'),
        ('chest', 'Chest'),
    )

    body_location = models.CharField(max_length=10, choices=BODY_LOCATIONS, blank=True, null=True)
    added_date=models.DateTimeField(auto_now=True)

class UserProfileService(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
