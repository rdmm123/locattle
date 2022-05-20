from rest_framework import serializers
from .models import CattleLocation

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CattleLocation
        fields = ('depto', 'farm', 'cow', 'lat', 'lng', 'timestamp')