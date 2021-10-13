from django.contrib import admin
from .models import ToDoList, Video
from embed_video.admin import AdminVideoMixin
from .models import Video
# Register your models here.

# By typing admin/ on your app site it will bring up admin dashboard.
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, MyModelAdmin)

admin.site.register(ToDoList)
