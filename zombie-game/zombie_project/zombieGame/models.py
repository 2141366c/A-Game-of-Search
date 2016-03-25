from django.db import models
from django.contrib.auth.models import User
# do we put badges in here ??? :S
# TRYING TO SLUG ACTIONS. MAYBE NEED TO MAKE A VIEW FOR THEM

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Stats and badges
    kills = models.IntegerField(default = 0)
    days = models.IntegerField(default = 1)
    people = models.IntegerField(default = 1)
    food = models.IntegerField(default = 3)
    ammo = models.IntegerField(default = 2)
    time = models.IntegerField(default = 100)

    survivorBadge = models.IntegerField(default = 0)
    killerBadge = models.IntegerField(default = 0)
    staminaBadge = models.IntegerField(default = 0)
    partyBadge = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.user.username

#class Fill_dict(models.Model):
 #   turn = models.CharField(max_length=30)
  #  s = models.SlugField(editable=True)

   # def save(self):
    #    if not self.id:
     #       self.s = slugify(self.options)

      #  super(turn, self).save()

 #   def __unicode__(self):
  #             return self.options

