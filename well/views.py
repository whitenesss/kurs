from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from well.models import Well
from well.serliazers import WellSerializer
from rest_framework.response import Response

# Create your views here.
class WellViewSet(viewsets.ViewSet):


    serializer_class = WellSerializer
    queryset = Well.objects.all()

    @action(detail=False, methods=['post'])
    def custom_action(self, request):
        # Custom logic here
        return Response({'status': 'custom post request'})
