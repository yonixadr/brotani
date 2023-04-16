from django.db import models


class FileUpload(models.Model):
    user = models.ForeignKey(
        'api.User', on_delete=models.CASCADE, related_name='upload')
    name = models.CharField(max_length=20)
    file = models.FileField()

    def __str__(self):
        return self.name
