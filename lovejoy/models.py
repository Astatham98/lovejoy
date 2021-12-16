from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import auth
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class User(auth.models.User,auth.models.PermissionsMixin):
     def __str__(self):
        return "@{}".format(self.username)

class Evaluation(models.Model):
    class Contact(models.TextChoices):
        EMAIL = 'email', "Email"
        PHONE = 'phone', "Phone"
    
    evaluation_text = models.TextField()
    contact_choice = models.CharField(max_length=5, choices=Contact.choices, default=Contact.EMAIL)
    image=models.ImageField(upload_to='images/', null=True, blank=True)
    user=models.CharField(max_length=150)

    def __str__(self):
        return self.evaluation_text
    