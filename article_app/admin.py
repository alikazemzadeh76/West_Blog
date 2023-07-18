from django.contrib import admin
from .models import Article, Category, Comment, Like
from . import models


class FilterByTitle(admin.SimpleListFilter):
    title = 'نام مقاله'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ('american', 'آمریکن'),
            ('germany', 'آلمانی'),
            ('french', 'فرانسوی'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


class CommentInLine(admin.StackedInline):
    model = models.Comment

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'shamsidate', 'show_image')
    list_filter = (FilterByTitle,)
    search_fields = ('title',)
    inlines = (CommentInLine,)



admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Comment)
