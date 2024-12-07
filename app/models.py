from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from cloudinary.models import CloudinaryField

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.avatar = "https://t4.ftcdn.net/jpg/05/49/98/39/360_F_549983970_bRCkYfk0P6PP5fKbMhZMIb07mCJ6esXL.jpg"
        user.save()
        return user

    def create_superuser(self, email, **extra_fields):
        extra_fields.setdefault('role', Role.ADMIN)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, **extra_fields)


class Role(models.TextChoices):
    ADMIN = 'Admin'
    USER = 'User'

class User(AbstractUser):
    password = models.CharField(max_length=128, null=True)
    username = None
    email = models.EmailField(blank=False, unique=True, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    avatar = CloudinaryField('image', null=False, blank=False)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)

    objects = UserManager()
