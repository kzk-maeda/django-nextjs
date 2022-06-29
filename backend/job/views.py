from django.shortcuts import render
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