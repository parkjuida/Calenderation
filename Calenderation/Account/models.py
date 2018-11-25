from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ChroniclerManager(BaseUserManager):
    def create_user(self, email, name, password, date_of_birth):
        if not email:
            raise ValueError('Users must have an email address')

        new_user = Chronicler(
            email_address=email,
            name=name,
            birth_date=date_of_birth
        )

        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, email_address, name, password):
        user = self.create_user(email_address, name, password, None)
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Chronicler(AbstractBaseUser, PermissionsMixin):
    email_address = models.EmailField(
        max_length=255,
        unique=True
    )
    name = models.CharField(
        max_length=63,
        default=""
    )
    password = models.CharField(
        max_length=127)

    birth_date = models.DateField(null=True)
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(default=False)

    objects = ChroniclerManager()

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email_address

    @property
    def is_staff(self):
        return self.is_superuser

    def get_full_name(self):
        full_name = '%s %s'