from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile/%Y/%m',default='default_img/default_img.jpg')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

