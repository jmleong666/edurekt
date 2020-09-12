from django.db import models

class Module(models.Model):
    code = models.CharField(primary_key=True, max_length=16, blank=False)
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=False)
    exam_time = models.DateTimeField(blank=True)

    def __str__(self):
         return self.code

