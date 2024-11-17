from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .models import Todo
from .serializers import TodoSerializer


class TodoAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [JWTAuthentication]

    
    def get(self, request):
        todo = Todo.objects.filter(user=request.user.id)
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(request=TodoSerializer)
    def post(self, request):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [JWTAuthentication]

    def get_objects(self, todo_id, user_id):
        try:
            return Todo.objects.get(id=todo_id, user=user_id)
        except Todo.DoesNotExist:
            return None
        
    def get(self, request, todo_id):
        todo_instance = self.get_objects(todo_id, request.user.id)
        if not todo_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # update
    def put(self, request, todo_id):
        todo_instance = self.get_objects(todo_id, request.user.id)
        if not todo_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'user': request.user.id
        }
        serializer = TodoSerializer(isinstance=todo_instance, 
                                    data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, todo_id):
        todo_instance = self.get_objects(todo_id, request.user.id)
        if not todo_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        todo_instance.delete()
        return Response(status=status.HTTP_200_OK)
    