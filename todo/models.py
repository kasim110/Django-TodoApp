from django.db import models
from users.models import User

class TodoTaskModel(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='user_todotask')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False)
    scheduled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
