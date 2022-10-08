from django.db import models




# Create your models here.
class Todo(models.Model):
    user=models.CharField(max_length=20,primary_key=True,verbose_name="User")
    task=models.CharField(max_length=10,verbose_name="task",blank=False)



