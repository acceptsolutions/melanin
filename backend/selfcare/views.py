from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SelfcareSerializer
from .models import Selfcare
# Create your views here.

class SelfcareView(viewsets.ModelViewSet):
    serializer_class = SelfcareSerializer
    queryset = Selfcare.objects.all()