from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500)
    about = models.CharField(max_length=1000)
    slogan = models.CharField(max_length=500)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    def __str__(self):
        return self.user.username

class Gig(models.Model):
    CATEGORY_CHOICES = (
    ("GD","Graphics & Design"),
    ("PT","Programming  & Tech"),
    ("DM","Digital and Marketing"),
    ("VA","Video & Animation"),
    ("MA","Music and Audio"),
    ("VM","Video & Marketing")
    )

    title = models.CharField(max_length = 500)
    category = models.CharField(max_length = 2,choices=CATEGORY_CHOICES)
    description = models.CharField(max_length = 1000)
    price = models.IntegerField(default = 6)
    photo = models.FileField(upload_to = 'gigs')
    status = models.BooleanField(default = True)
    user = models.ForeignKey(User,on_delete = models.DO_NOTHING )
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
      return self.title
