from django.contrib import admin
from .models import Setting, ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject','update_at',]
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip',)
    list_filter = ['status']

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','about']
# Register your models here.
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Setting, SettingAdmin)
