from .import views
from django.urls import path,include
from .views import create_account, login_user

app_name = 'Existingapp'
urlpatterns = [
    path('create_account/', create_account, name='create_account'),
    path('login/', login_user, name='login'),
    path('tattoo/service/',views.TattooServiceView.as_view(), name='tattoo-service'),
    path('tattoo/head/', views.TattooHeadView.as_view(), name='tattoo-head'),
    path('tattoo/neck/',views.TattooNeckView.as_view(), name='tattoo-neck'),
    # Add more URL patterns for other tattoo-related views as needed
]
