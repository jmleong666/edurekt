from django.db import models

class Cca(models.Model):
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name