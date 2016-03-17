from django.db import models

class Status(models.Model):
    zombies_killed = models.IntegerField(default = 0)
    ammo = models.IntegerField(default = 0)
    food = models.IntegerField(default = 10)
    days_alive = models.IntegerField(default = 0)
    party_size = models.IntegerField(default = 1)
	
    def __unicode__(self):
	    return self.days_alive

class Badges(models.Model):
    survivor = models.IntegerField(default = 0)
    killer = models.IntegerField(default = 0)
    stamina = models.IntegerField(default = 0)
    party = models.IntegerField(default = 0)
	
    def __unicode__(self):
	    return self.survivor
	
class Player(models.Model):
    username = models.CharField(max_length = 128, unique = True)
    status = models.ForeignKey(Status)
    badges = models.ForeignKey(Badges)
	
    def __unicode__(self):
	    return self.username