from django.urls import path

from app.views import IPListCreateAPIView

urlpatterns = [
    path('ip/', IPListCreateAPIView.as_view())
]
