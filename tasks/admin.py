from django.contrib import admin
from .models import CustomUser, Task
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    fields = ['username', 'email']

class TaskAdmin(admin.ModelAdmin):
    fields = ['user', 'task_name', 'task_description', 'end_date']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)
