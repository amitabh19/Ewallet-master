from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Transactions(models.Model):
    rmob = models.IntegerField(max_length=11 , primary_key=True)
    smob = models.IntegerField(max_length=11)
    tdate = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(max_length=100000)
    balance = models.IntegerField(max_length=1000000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TransactionsLog(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        rmob = models.ForeignKey(Transactions, on_delete=models.CASCADE)
        smob = models.IntegerField(max_length=11)
        tdate = models.DateTimeField(default=timezone.now)
        amount = models.IntegerField(max_length=100000)


class UserProfile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    mob = models.CharField(max_length=14, default='')


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


