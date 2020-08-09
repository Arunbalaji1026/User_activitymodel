from django.urls import path
from rest_framework import routers, serializers

from .views import ActivityPeriodList

urlpatterns = [
    path("activities", ActivityPeriodList.as_view(), name="activities")
]
