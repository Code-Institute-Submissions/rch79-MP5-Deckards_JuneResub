from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    '''
    User profile model to store delivery information
    and order history
    '''

    'Only one profile per user and only one user per profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=24, null=True, blank=True)
    default_address_line1 = models.CharField(max_length=80, null=True, blank=True)
    default_address_line2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=24, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label="Country", null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    '''
    Create or update uer profile
    '''

    if created:
        UserProfile.objects.create(user=instance)
    # for existing users, profile is updated
    instance.userprofile.save()
