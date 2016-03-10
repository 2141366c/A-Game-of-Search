from django.db import models

class Player(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    days_alive = models.IntegerField(default = 0)
    zombies_killed = models.IntegerField(default = 0)
    ammo = models.IntegerField(default = 0)
    food = models.IntegerField(default = 0)