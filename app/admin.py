from django.contrib import admin
from app.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
      list_display=('task','is_completed')
      search_fields=('task',)
admin.site.register(Task,TaskAdmin)