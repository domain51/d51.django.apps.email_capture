from django.contrib.auth.models import User
from django.db import models
from d51.django.apps.email_capture import managers

class EmailAddress(models.Model):
    email = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.email

