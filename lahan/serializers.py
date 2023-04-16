from rest_framework import serializers
from django.contrib.auth.models import User
from lahan.models import lahan


class LahanSerializer(serializers.ModelSerializer):
    imgGreenhouse = serializers.FileField(required=False)

    class Meta:
        model = lahan
        fields = ('user', 'nameGreenhouse', 'addressGreenhouse', 'luas', 'komoditas', 'jml_bibit', 'long', 'lat', 'imgGreenhouse', 'nib',
                  'mitra', 'created_at', 'update_at')
