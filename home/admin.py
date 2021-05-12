from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfile


class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status','note']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','address','city','country','image_tag' ]



admin.site.register(Setting,SettingtAdmin)
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(UserProfile,UserProfileAdmin)

