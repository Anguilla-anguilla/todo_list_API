from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('api/', views.TodoAPIView.as_view()),
    path('api/<int:todo_id>', views.TodoDetailAPIView.as_view()),
]
