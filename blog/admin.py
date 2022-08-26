from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):

    date_hierarchy = 'created_at'
    empty_date_hierarchy = 'empty'
    list_display = ('title', 'author', 'content_view', 'status',
                    'published_at', 'created_at', 'updated_at')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')
    summernote_fields = ('content',)

    class Meta:
        ordering = ['-created_at']
        admin.site.register(Category)


admin.site.register(Post, PostAdmin)
