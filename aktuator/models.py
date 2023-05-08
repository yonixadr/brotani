from django.db import models

# Create your models here.


class aktuator(models.Model):
    user = models.ForeignKey(
        'api.User', on_delete=models.CASCADE, related_name='aktuator')
    kipas_angin = models.BooleanField(default=False)
    pompa_air = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"
