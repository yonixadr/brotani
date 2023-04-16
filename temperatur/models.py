from django.db import models

# Create your models here.


class temperatur(models.Model):
    user = models.ForeignKey(
        'api.User', on_delete=models.CASCADE, related_name='temperatur')
    kelembapan_udara = models.CharField(max_length=255, blank=True, null=False)
    kelembapan_tanah = models.CharField(max_length=255, blank=True, null=False)
    cahaya = models.CharField(max_length=255, blank=True, null=False)
    suhu_udara = models.CharField(max_length=255, blank=True, null=False)
    suhu_tanah = models.CharField(max_length=255, blank=True, null=False)
    ph = models.CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return f"{self.id}"
