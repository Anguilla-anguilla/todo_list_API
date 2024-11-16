from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    description = models.TextField(verbose_name='description')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='user_fk')
    
    def __str__(self):
        return self.title
    

