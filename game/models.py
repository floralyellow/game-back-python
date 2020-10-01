from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    id = int
    creationDate = datetime.date
    login = models.TextField()
    password = models.TextField()
 
    def _str_(self):
        return self.title


class Session(models.Model):
    id = int
    creationDate = datetime.date
    id_user = int
    nb_room = int
    name = models.TextField()


class Room(models.Model):
    id = int
    id_session = int
    order = int
    is_special = bool
    is_done = bool


class RoomMonsters(models.Model):
    id = int
    id_room = int
    id_monster = int


class Monster(models.Model):
    id = int
    name = models.TextField
    life_point = int
    damage = int
