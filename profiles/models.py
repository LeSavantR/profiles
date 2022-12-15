import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

# Local Model User
class UserProfileManager(BaseUserManager):
    """ Manager User Profiles """

    def create_user(self, email:str, name:str, password:str):
        if not email:
            raise ValueError('Usuario debe tener un E-Mail')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email:str, name:str, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ New Model User for DataBase System """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField(
        verbose_name='E-Mail',
        max_length=255, unique=True,
        help_text='username@example.com'
    )
    name = models.CharField(
        verbose_name='Nombres de Usuario',
        max_length=100,
        help_text='Nombres de la persona.'
    )
    last_name = models.CharField(
        verbose_name='Apellidos de Usuario',
        max_length=200,
        help_text='Apellidos de la persona.'
    )
    is_active = models.BooleanField(
        verbose_name='Is Active?',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Is Staff?',
        default=False
    )
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self) -> str:
        """ Get Fully Name User """
        return f'{self.name} {self.last_name}'

    def get_short_name(self) -> str:
        """ Get Shorty Name User """
        return f'{self.name}'

    def __str__(self) -> str:
        """ Get Model Instance """
        return f'{self.email}'

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'
