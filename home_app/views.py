from django.shortcuts import render
from django.utils.text import slugify
from article_app.models import Article
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('date')[:3]
        return context


def sidebar(request):
    return render(request, 'includes/sidebar.html')






