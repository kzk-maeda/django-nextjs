from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
  class Meta:
    model = Job
    fields = '__all__'