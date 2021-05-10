from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from job.models import Category, Job, Images


class JobImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_jobs_count','related_jobs_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Job,
                'category',
                'jobs_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Job,
                 'category',
                 'jobs_count',
                 cumulative=False)
        return qs

    def related_jobs_count(self, instance):
        return instance.jobs_count
    related_jobs_count.short_description = 'Related jobs (for this specific category)'

    def related_jobs_cumulative_count(self, instance):
        return instance.jobs_cumulative_count
    related_jobs_cumulative_count.short_description = 'Related jobs (in tree)'

class JobAdmin(admin.ModelAdmin):
    list_display = ['title','salary','company','location','image_tag','category']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [JobImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','job','image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Images,ImagesAdmin)
