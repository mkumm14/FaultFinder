from django.db import models
from django.core.validators import FileExtensionValidator

from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        default="default-profile-pic.png",
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
        width_field='picture_width',
        height_field='picture_height'
    )
    picture_width = models.PositiveIntegerField(default=1000, editable=False)
    picture_height = models.PositiveIntegerField(default=1000, editable=False)

    def __str__(self):
        return f"{self.user}'s profile"