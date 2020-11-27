from django.contrib import admin
from .models import *
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'status', 'create_at']
    list_filter = ['status']
    readonly_fields = ('subject', 'comment', 'ip', 'user', 'article', 'rate',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_at']
    list_filter = ['title']

class ArticleImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_at', 'image']
    list_filter = ['title']
    readonly_fields = ('image',)
    inlines = [ArticleImageInline]

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Images)