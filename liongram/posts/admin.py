from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num  =3
    max_num = 5
    verbose_name = "댓글"
    verbose_name_plural = "댓글"


# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    #list_editable = ('content', )
    list_Filter=('created_at',)
    search_fields = ('id', 'writer__username',)
    readonly_fields = ('created_at',)
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    inlines = [CommentInline]

    actions = []

# admin.site.register(Comment)
