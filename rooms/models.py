from django.db import models

class Room(models.Model):
    code = models.CharField(max_length=32, blank=False)
    name = models.CharField(max_length=256, blank=False)
    address = models.TextField(blank=False)
    max_capacity = models.year = models.PositiveSmallIntegerField(blank=False)

    def __str__(self):
        return self.name
