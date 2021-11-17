from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    endpoint = {
        'test':'test1'
    }

    return Response(endpoint)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    task = get_object_or_404(Task,pk=pk)
    # task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)

    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT','PATCH'])
def taskUpdate(request,pk):
    task = get_object_or_404(Task,pk=pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()

    return Response('Task deleted successfully')



