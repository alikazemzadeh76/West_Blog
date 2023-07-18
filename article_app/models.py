from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify
from jdatetime import datetime as jdatetime


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    credited = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    slug = models.SlugField(null=True, unique=True, blank=True, verbose_name="عنوان صفحه")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()


    def get_categories_url(self):
        return reverse("blog:category_detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="نویسنده")
    category = models.ManyToManyField(Category, related_name='article', verbose_name="دسته بندی")
    title = models.CharField(max_length=50, verbose_name="عنوان" )
    description = models.TextField( verbose_name="توضیحات")
    image = models.ImageField(upload_to='image/article_app', verbose_name="عکس")
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, verbose_name="آخرین بروز رسانی")
    slug = models.SlugField(null=True, unique=True, blank=True, verbose_name="عنوان صفحه")

    def shamsidate(self):
        gdate = self.update.date()
        jdate = jdatetime.fromgregorian(date=gdate)
        return jdate.strftime('%Y/%m/%d')

    shamsidate.short_description = "آخرین بروز رسانی"  #برای تغییر نام در پنل ادمین

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        return ('<h2 style="container: revert">این مقاله تصویر ندارد</h2>')

    show_image.short_description = 'تصویر'

    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()
    

    def get_absolute_url(self):
        return reverse("blog:post_view", kwargs={'slug': self.slug})


    def __str__(self):
        return f"{self.title} - {self.description[:40]}"

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="کاربر")
    body = models.TextField( verbose_name="متن کامنت")
    created_time = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE, related_name='replies', verbose_name="پاسخ به")

    def __str__(self):
        return self.body[:50]
    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like', verbose_name='مقاله')

    def __str__(self):
        return f'{self.user.username} - {self.article.title}'


    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'






















