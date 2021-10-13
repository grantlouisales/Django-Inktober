from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class User(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    prompt = models.CharField(max_length=200)

    def __str__(self):
        return self.fname + self.lname

class Video(models.Model):
    video = EmbedVideoField()
