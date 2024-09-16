from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duedate = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


