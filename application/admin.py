from django.contrib import admin

# Register your models here.
from application.models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'salary', 'company', 'title','status']
    list_filter = ['user']


admin.site.register(Application,ApplicationAdmin)