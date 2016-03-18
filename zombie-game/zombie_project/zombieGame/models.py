from django.db import models
from django.contrib.auth.models import User
# do we put badges in here ??? :S

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)


    def __unicode__(self):
        return self.user.username