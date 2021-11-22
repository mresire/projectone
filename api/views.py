from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer,TaskCreateSerializer
from rest_framework import status

from .permissions import IsOwnerOrReadOnly

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)


from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    
    )

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

'''
Function based view
'''

class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','is_completed']
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     # qs=Task.objects.filter(user=self.request.user)
    #     return self.queryset.filter(user=self.request.user)



class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes =[IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field ='id'
    lookup_url_kwarg='id'

class TaskUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field ='id'
    lookup_url_kwarg='id'
    permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class TaskDeleteAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field ='id'
    lookup_url_kwarg='id'


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field ='id'
    lookup_url_kwarg='id'








