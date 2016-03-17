from django.db import models
	
class Player(models.Model):
    username = models.CharField(max_length = 128, unique = True)
    zombiesKilled = models.IntegerField(default = 0)
    ammo = models.IntegerField(default = 2)
    food = models.IntegerField(default = 3)
    daysAlive = models.IntegerField(default = 1)
    partySize = models.IntegerField(default = 1)
    survivorBadge = models.IntegerField(default = 0)
    killerBadge = models.IntegerField(default = 0)
    staminaBadge = models.IntegerField(default = 0)
    partyBadge = models.IntegerField(default = 0)
	
    def __unicode__(self):
	    return self.username