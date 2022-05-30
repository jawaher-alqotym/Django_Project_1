from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_filter = ('user',)


admin.site.register(Task,TaskAdmin)
admin.site.register(VrSpace)
