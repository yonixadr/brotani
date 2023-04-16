from random import randint
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from hashlib import sha256
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, telephone, address):
        if not email:
            raise ValueError('Users Must Have an email address')
        salt = randint(0, 99999)
        user = self.model(
            username=username,
            telephone=telephone,
            address=address,
            email=self.normalize_email(email),
            hash_string=sha256(
                (f'{str(salt)}{password}').encode('utf-8')).hexdigest()
        )

        print(password)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=False,
        null=False,

    )
    username = models.CharField(
        max_length=50, unique=True, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=False)
    address = models.CharField(max_length=255, blank=True, null=False)

    hash_string = models.CharField(max_length=200, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return "{}".format(self.email)
