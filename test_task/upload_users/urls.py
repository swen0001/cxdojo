from django.urls import path
from .views import index, upload

app_name = 'upload_user'

urlpatterns = [
    path('', index),
    path('upload/', upload),
]
