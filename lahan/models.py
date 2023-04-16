from django.db import models
import uuid


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s/%s" % (uuid.uuid4(), ext)
    return 'images/{filename}'.format(filename=filename)


# Create your models here.


class lahan(models.Model):
    user = models.ForeignKey(
        'api.User', on_delete=models.CASCADE, related_name='lahan')
    # nik = models.CharField(max_length=255, blank=True, null=False)
    # fullname = models.CharField(max_length=255, blank=True, null=False)
    # telephone = models.CharField(max_length=255, blank=True, null=False)
    # address = models.CharField(max_length=255, blank=True, null=False)
    nameGreenhouse = models.CharField(max_length=255, blank=True, null=False)
    addressGreenhouse = models.CharField(
        max_length=255, blank=True, null=False)
    luas = models.CharField(max_length=255, blank=True, null=False)
    komoditas = models.CharField(max_length=255, blank=True, null=False)
    jml_bibit = models.CharField(max_length=255, blank=True, null=False)
    mitra = models.CharField(max_length=255, blank=True, null=False)
    long = models.FloatField(max_length=255, blank=True, null=True)
    lat = models.FloatField(max_length=255, blank=True, null=True)
    imgGreenhouse = models.ImageField(
        upload_to='images/', blank=True, null=True)
    nib = models.CharField(max_length=255, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"


# class LahanImage(models.Model):
#     lahan = models.ForeignKey(
#         Lahan, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='images/', blank=True, null=True)

#     def __str__(self):
#         return f"{self.lahan.id}"
