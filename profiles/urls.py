from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('addprofile/', views.add_profile, name='add-profile'),
    path('<int:pk>/updateprofile/', views.update_profile, name='update-profile'),
]
