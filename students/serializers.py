from rest_framework import serializers

from modules.models import Module
from ccas.models import Cca
from students.models import Student, TakeModule, TakeCca


class StudentSerializer(serializers.ModelSerializer):
    modules = serializers.PrimaryKeyRelatedField(many=True, queryset=Module.objects.all(), read_only=False)

    class Meta:
        model = Student
        fields = ('matriculation_number', 'name', 'year', 'course', 'modules')


class TakeModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeModule
        fields = ('module', 'student')

class TakeCcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeCca
        fields = ('cca', 'student')