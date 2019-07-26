from rest_framework import serializers
from .models import Selfcare

class SelfcareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selfcare
        fields = ('id', 'title', 'description', 'post')