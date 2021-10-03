from django.contrib import admin
from .models import ToDoList
# Register your models here.

# By typing admin/ on your app site it will bring up admin dashboard.
admin.site.register(ToDoList)