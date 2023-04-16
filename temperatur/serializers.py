from rest_framework import serializers
from django.contrib.auth.models import User
from temperatur.models import temperatur


class TemperaturSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperatur
        fields = ('user', 'cahaya', 'kelembapan_tanah',
                  'kelembapan_udara', 'suhu_udara', 'suhu_tanah', 'ph')
