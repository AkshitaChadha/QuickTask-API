from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
  permission_classes= [IsAuthenticated]
  queryset= Task.objects.all()
  serializer_class= TaskSerializer
