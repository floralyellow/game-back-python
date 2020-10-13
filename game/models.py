from django.db import models
from django.contrib.auth.models import User


class Session(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    nb_room = models.IntegerField(null=False)
    name = models.TextField()


class Room(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE,)
    order = models.IntegerField(null=False)
    is_special = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)


class Monster(models.Model):
    name = models.CharField(max_length=200, unique=True)
    life_point = models.IntegerField(null=False)
    damage = models.IntegerField(null=False)


class RoomMonster(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE,)
    monster = models.OneToOneField(Monster, on_delete=models.CASCADE,)
    life_point_left = models.IntegerField(null=True)


class Character(models.Model):
    name = models.CharField(max_length=200, unique=True)
    special_effect = models.TextField()


class SessionCharacters(models.Model):
    life_point = models.IntegerField(null=False)
    max_life_point = models.IntegerField(null=False)
    session = models.OneToOneField(Session, on_delete=models.CASCADE,)
    character = models.OneToOneField(Character, on_delete=models.CASCADE,)
    level = models.IntegerField(null=False, default=1)
    is_alive = models.BooleanField(default=True)


class TypeAttack(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Attacks(models.Model):
    name = models.CharField(max_length=200, unique=True)
    damage = models.IntegerField(null=False)
    critical = models.IntegerField(null=False)
    critical_chance = models.IntegerField(null=False)
    is_zone = models.BooleanField(default=False)
    type = models.ForeignKey(TypeAttack, on_delete=models.CASCADE,)
    character = models.ForeignKey(Character, on_delete=models.CASCADE,)


class SessionCharactersAttacks(models.Model):
    session_character = models.OneToOneField(SessionCharacters, on_delete=models.CASCADE,)
    attack = models.OneToOneField(Attacks, on_delete=models.CASCADE,)
    nb_bonuses = models.IntegerField(null=True, default=0)


class Bonuses(models.Model):
    type_attack = models.ForeignKey(TypeAttack, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, unique=True)
    add_attack = models.IntegerField(null=True, default=10)


class Round(models.Model):
    num_round = models.IntegerField(null=True, default=1)
    is_finished = models.BooleanField(default=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,)


class Action(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE,)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE,)
    session_character = models.ForeignKey(SessionCharacters, on_delete=models.CASCADE,)
    is_monster_turn = models.BooleanField(default=False)
    damage = models.IntegerField(null=True)
    session_character_attack = models.ForeignKey(SessionCharactersAttacks, on_delete=models.CASCADE,)
    is_critical = models.BooleanField(default=False)

