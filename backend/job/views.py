from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer

# Create your views here.
@api_view(['GET'])
def getAllJobs(request: Request) -> Response:
  jobs = Job.objects.all()
  serializer = JobSerializer(jobs, many=True)

  return Response(serializer.data)


@api_view(['GET'])
def getJob(request: Request, pk: int) -> Response:
  job = get_object_or_404(Job, id=pk)
  serializer = JobSerializer(job, many=False)

  return Response(serializer.data)


@api_view(['POST'])
def newJob(request: Request) -> Response:
  data = request.data

  job = Job.objects.create(**data)
  serializer = JobSerializer(job, many=False)

  return Response(serializer.data)


@api_view(['PUT'])
def updateJob(request: Request, pk: int) -> Response:
  job = get_object_or_404(Job, id=pk)

  job.title = request.data['title']
  job.description = request.data['description']
  job.email = request.data['email']
  job.address = request.data['address']
  job.jobType = request.data['jobType']
  job.education = request.data['education']
  job.industry = request.data['industry']
  job.experience = request.data['experience']
  job.salary = request.data['salary']
  job.positions = request.data['positions']
  job.company = request.data['company']

  job.save()

  serializer = JobSerializer(job, many=False)

  return Response(serializer.data)