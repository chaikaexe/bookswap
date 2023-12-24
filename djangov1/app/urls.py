from django.urls import path
from . import views
from .views import RegisterView

app_name = 'app'

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
]