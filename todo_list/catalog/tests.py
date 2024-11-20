# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from .models import Todo
# from .serializers import TodoSerializer


# class TodoListViewTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser',
#                                               email='e@mail.com',
#                                               password='testpassword')
#         self.client.force_authenticate(user=self.user)
#         self.todo = Todo.objects.create(title='Test Todo',
#                                         description='Test description',
#                                         user=self.user)
        
#     def test_get_todo(self):
#         url = reverse('api')
#         response = self.client.get(url)
#         todo_list = Todo.objects.filter(user=self.user)
#         serializer = TodoSerializer(todo_list, mamy=True)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
