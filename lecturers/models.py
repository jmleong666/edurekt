from django.db import models

class Lecturer(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=16, blank=False)
    name = models.CharField(max_length=256, blank=False)
    department = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.name