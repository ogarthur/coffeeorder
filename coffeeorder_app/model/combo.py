#-*- coding: utf-8 -*-

from django.db import models


class Combo(models.Model):
    class Meta:
        pass

    combo_prize = models.IntegerField()


