from django.db import models
from django.contrib.auth.models import AbstractUser
from io import BytesIO
from PIL import Image
from core.settings import BASE_URL
from django.core.files import File

# Create your models here.


class CustomUser(AbstractUser):
    ROLES = [
        ('AD', 'Admin'),
        ('PU', 'Power user'),
        ('NU', 'Normal user')
    ]
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=2, choices=ROLES, default='NU')
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def save(self, *args, **kwargs):
        if not self.thumbnail:
            if self.avatar:
                self.thumbnail = self.make_thumbnail(self.avatar)
                self.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username

    def thumbnail_url(self):
        return BASE_URL + self.thumbnail.url

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)
        return File(thumb_io, name=image.name)
