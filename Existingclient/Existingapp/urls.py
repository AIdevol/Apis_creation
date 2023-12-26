from .import views
from django.urls import path,include
from .views import create_account, login_user

app_name = 'Existingapp'
urlpatterns = [
    path('create_account/', create_account, name='create_account'),
    path('login/', login_user, name='login'),
    
]