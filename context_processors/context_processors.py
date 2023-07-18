from article_app.models import Article, Category
from django.shortcuts import get_object_or_404
from jdatetime import datetime as jdatetime

def resent_post(request):
    sidebar_article = Article.objects.all().order_by('-date')[:3]

    def shamsidate(self):
        gdate = self.update.date()
        jdate = jdatetime.fromgregorian(date=gdate)
        return jdate.strftime('%Y/%m/%d')

    return {'sidebar_article': sidebar_article}


def category_options(request):
    categoories = Category.objects.all()
    return {'categories': categoories}