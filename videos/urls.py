from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_video, name='video-create'),
    path('<int:pk>/', views.detail_video, name='video-detail'),
    path('<int:pk>/update', views.update_video, name='video-update'),
    path('<int:pk>/delete', views.DeleteVideo.as_view(), name='video-delete'),
    path('category/<int:pk>', views.video_category_list, name='category-list'),
    path('search/', views.search_video, name='video-search'),
]
