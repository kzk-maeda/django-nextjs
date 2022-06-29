from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count

from .models import Job
from .serializers import JobSerializer
from .filters import JobsFilter

# Create your views here.
@api_view(['GET'])
def getAllJobs(request: Request) -> Response:
  filterset = JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))
  serializer = JobSerializer(filterset.qs, many=True)

  return Response(serializer.data)


@api_view(['GET'])
def getJob(request: Request, pk: int) -> Response:
  job = get_object_or_404(Job, id=pk)
  serializer = JobSerializer(job, many=False)

  return Response(serializer.data)


@api_view(['POST'])
def newJob(request: Request) -> Response:
  data = request.data

  serializer = JobSerializer(data=data)
  if serializer.is_valid():
    job = serializer.save()

  return Response(serializer.data)


@api_view(['PUT'])
def updateJob(request: Request, pk: int) -> Response:
  job = get_object_or_404(Job, id=pk)
  data = request.data

  serializer = JobSerializer(job, data=data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)


@api_view(['DELETE'])
def deleteJob(request: Request, pk: int) -> Response:
  job = get_object_or_404(Job, id=pk)

  job.delete()

  return Response({ 'message': 'Job is Deleted.' }, status=status.HTTP_200_OK)


@api_view(['GET'])
def getTopicStats(request: Request, topic: str) -> Response:
  args = { 'title__icontains': topic }
  jobs = Job.objects.filter(**args)

  if len(jobs) == 0:
    return Response({ 'message': f'Not stats found for {topic}' })
  
  stats = jobs.aggregate(
    total_jobs = Count('title'),
    avg_positions = Avg('positions'),
    avg_salary = Avg('salary'),
    min_salary = Min('salary'),
    max_salary = Max('salary')
  )

  return Response(stats)