from rest_framework import serializers
from django.contrib.auth.models import User
from notifikasi.models import notifikasi


class NotifikasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = notifikasi
        fields = ('user', 'title', 'messages', 'link')
