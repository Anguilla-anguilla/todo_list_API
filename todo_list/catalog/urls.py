from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('api/', views.TodoAPIView.as_view(), name='api'),
    path('api/<int:todo_id>', views.TodoDetailAPIView.as_view(), name='api-id'),
    path('api/list/', views.TodoListView.as_view(), name='api-list')
]
