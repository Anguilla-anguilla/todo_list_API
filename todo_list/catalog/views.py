from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .models import Todo
from .serializers import TodoSerializer
from .pagination import CustomPageNumberPagination


class TodoListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [JWTAuthentication]
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


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
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # update
    @extend_schema(request=TodoSerializer)
    def put(self, request, todo_id):
        todo_instance = self.get_objects(todo_id, request.user.id)
        if not todo_instance:
            return Response(status=status.HTTP_403_FORBIDDEN)

        data = {'user': request.user.id}
        if request.data.get('title'):
            data['title'] = request.data.get('title')
        if request.data.get('description'):
            data['description'] = request.data.get('description')
        if request.data.get('mark_done'):
            data['mark_done'] = request.data.get('mark_done')

        serializer = TodoSerializer(instance=todo_instance,
                                    data=data, partial=True,
                                    context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, todo_id):
        todo_instance = self.get_objects(todo_id, request.user.id)
        if not todo_instance:
            return Response(status=status.HTTP_403_FORBIDDEN)
        todo_instance.delete()
        return Response(status=status.HTTP_200_OK)
    