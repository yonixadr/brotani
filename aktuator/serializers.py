from rest_framework import serializers
from django.contrib.auth.models import User
from aktuator.models import aktuator


class AktuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = aktuator
        fields = ('user', 'kipas_angin', 'pompa_air', 'created_at')
