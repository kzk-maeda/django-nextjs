from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Job
from .serializers import JobSerializer
from .filters import JobsFilter

# Create your views here.
@api_view(['GET'])
def getAllJobs(request: Request) -> Response:
  filterset = JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))

  count = filterset.qs.count()

  # Pagenation
  resPerPage = 3

  paginator = PageNumberPagination()
  paginator.page_size = resPerPage
  queryset = paginator.paginate_queryset(filterset.qs, request)

  serializer = JobSerializer(queryset, many=True)

  return Response({
    'count': count,
    'resPerPage': resPerPage,
    'jobs': serializer.data
  })


@api_view(['GET'])
def getJob(request: Request, pk: int) -> Response:
  job = get_object_or_404(Job, id=pk)
  serializer = JobSerializer(job, many=False)

  return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newJob(request: Request) -> Response:
  request.data['iser'] = request.user
  data = request.data

  serializer = JobSerializer(data=data)
  if serializer.is_valid():
    job = serializer.save()

  return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateJob(request: Request, pk: int) -> Response:
  job = get_object_or_404(Job, id=pk)
  if job.user != request.user:
    return Response({ 'message': 'You cannot update this job.' }, status=status.HTTP_403_FORBIDDEN)
  data = request.data

  serializer = JobSerializer(job, data=data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteJob(request: Request, pk: int) -> Response:
  job = get_object_or_404(Job, id=pk)
  if job.user != request.user:
    return Response({ 'message': 'You cannot delete this job.' }, status=status.HTTP_403_FORBIDDEN)


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