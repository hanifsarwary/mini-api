from django.urls import path
from .views import MyDetailsAPIView

urlpatterns = [
    path('me/', MyDetailsAPIView.as_view()),
]
