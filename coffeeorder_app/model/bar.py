#-*- coding: utf-8 -*-

from django.db import models
from .combo import Combo


class Bar(models.Model):
    class Meta:
        pass

    bar_name = models.CharField(max_length=100)
    bar_description = models.TextField(max_length=500, null=True, blank=True)
    bar_color = models.CharField(max_length=100, default="yellow")
    bar_official = models.BooleanField(default=False)

    def __str__(self):
        return 'BAR:{}'.format(self.bar_name)
