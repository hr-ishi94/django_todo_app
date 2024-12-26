from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length = 300)
    updated_date = models.DateField(auto_now = True)
    created_date = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.text + '--' + str(self.user)