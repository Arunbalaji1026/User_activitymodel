from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework import generics
#from django_filters.rest_framework import DjangoFilterBackend
#from django.contrib.sites.shortcuts import get_current_site
# Create your views here.

from .models import ActivityPeriod
from .serializers import ActivityPeriodSerializer


class ActivityPeriodList(generics.ListAPIView):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['level', 'server_IP', 'log_time']
    # def get(self, request, *args, **kwargs):
