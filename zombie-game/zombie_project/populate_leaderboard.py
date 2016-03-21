__author__ = 'dylanclark'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombie_project.settings')

import django
django.setup()

from django.contrib.auth.models import User
from zombieGame.models import UserProfile


def populate():

    add_user(username="Bob",
        password="Bob",
        email="bob@bob.com",
        days="20",
        kills="100")

    add_user(username="Jill",
        password="Jill",
        email="jill@jill.com",
        days="2",
        kills="7")

    add_user(username="Jen",
        password="Jen",
        email="jen@jen.com",
        days="50",
        kills="200")


def add_user(username, password, email, days, kills):
    u = User.objects.get_or_create(username=username, password=password, email=email)[0]
    up = UserProfile(user=u, days=days, kills=kills)
    up.save()



# Start execution here!
if __name__ == '__main__':
    populate()