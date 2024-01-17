from django.urls import path
from . import views

urlpatterns = [
    path('health-check/', views.health_check, name='health_check'),
    path('', views.UploadMediaFile.as_view(), name='upload_media_file'),
]
