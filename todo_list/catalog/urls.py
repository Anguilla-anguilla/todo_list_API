from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('api', views.TodoAPIView.as_view()),
]
