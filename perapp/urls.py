from django.urls import path, include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'users',views.UserViewSets)
router.register(r'groups',views.GroupViewSets)
router.register(r'permission',views.PermissionViewSets)

urlpatterns=[
    path('',include(router.urls))

]