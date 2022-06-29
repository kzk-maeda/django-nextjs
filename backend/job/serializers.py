from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
  class Meta:
    model = Job
    fields = '__all__'
  
  def create(self, data):
    '''
    Create new Job object in Database
    '''
    return Job.objects.create(**data)

  def update(self, job, data):
    '''
    Update spesific Job object
    '''
    job.title = data['title']
    job.description = data['description']
    job.email = data['email']
    job.address = data['address']
    job.jobType = data['jobType']
    job.education = data['education']
    job.industry = data['industry']
    job.experience = data['experience']
    job.salary = data['salary']
    job.positions = data['positions']
    job.company = data['company']

    job.save()
    return job