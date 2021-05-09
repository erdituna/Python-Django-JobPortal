from django.contrib import admin

# Register your models here.
from job.models import Category, Job, Images


class JobImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class JobAdmin(admin.ModelAdmin):
    list_display = ['title','salary','company','location','category']
    list_filter = ['status','category']
    inlines = [JobImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','job','image']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Images,ImagesAdmin)
