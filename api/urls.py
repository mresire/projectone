from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',apiOverview,name='api-overview'),
    path('task-list/',taskList,name='task-list'),
    path('task-detail/<int:pk>/',taskDetail,name='task-detail'),
    path('task-create/',taskCreate,name='task-create'),
    path('task-update/<int:pk>/',taskUpdate,name='task-update'),
    path('task-delete/<int:pk>/',taskDelete,name='task-delete'),

    path('v1/',TaskListAPIView.as_view(),name='task-list-v1'),
    path('v1/task-create/',TaskCreateAPIView.as_view(),name='task-create-v1'),
    path('v1/task-detail/<int:id>/',TaskDetailAPIView.as_view(),name='task-detail-v1'),
    path('v1/task-update/<int:id>/',TaskUpdateAPIView.as_view(),name='task-update-v1'),
    path('v1/task-delete/<int:id>/',TaskDeleteAPIView.as_view(),name='task-delete-v1'),

    path('v2/',TaskListCreateAPIView.as_view(),name='task-list-v2'),
    path('v2/<int:id>',TaskDetailUpdateDestroyAPIView.as_view(),name='task-detail-v2'),

]