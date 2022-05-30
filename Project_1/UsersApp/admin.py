from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'first_name', 'last_name', 'email')
    date_hierarchy = 'registration_date'
    search_fields = ['user_name']


admin.site.register(User, UserAdmin)


