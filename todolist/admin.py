from django.contrib import admin

from todolist.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "title", "description", "done", "owner")
    list_filter = ("created", "done", "owner")
