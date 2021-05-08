from django.contrib import admin

# Register your models here.
from job.models import Category, Job


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class JobAdmin(admin.ModelAdmin):
    list_display = ['title','salary','company','location','category']
    list_filter = ['status','category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Job,JobAdmin)