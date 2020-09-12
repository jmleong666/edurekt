from django.db import models

from modules.models import Module


class Student(models.Model):
    matric_number = models.CharField(primary_key=True, max_length=9, blank=False)
    name = models.CharField(max_length=256, blank=False)
    year = models.PositiveSmallIntegerField(blank=False, default=1)
    course = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.name

class TakeModules(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
