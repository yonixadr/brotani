from django.db import models

# Create your models here.


class notifikasi(models.Model):
    user = models.ForeignKey(
        'api.User', on_delete=models.CASCADE, related_name='notifikasi')
    title = models.CharField(max_length=255, blank=True, null=False)
    messages = models.CharField(max_length=255, blank=True, null=False)
    link = models.CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return f"{self.id}"
