from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Article, Category, Comment, Like
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView


class ArticleView(DetailView):
    model = Article
    template_name = 'article_app/post-details.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.user.like.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True

        else:
            context['is_liked'] = False
        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        message = request.POST.get('message')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=message, article=article, user=request.user, parent_id=parent_id)


        return redirect('blog:post_view', slug=article.slug)


class AllPostView(ListView):
    model = Article
    template_name = 'article_app/all_article.html'
    context_object_name = 'object_list'
    paginate_by = 2





def all_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    articles = category.article.all()
    return  render(request, 'article_app/all_article.html', {'object_list': articles})


class AllCategoryView(ListView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        category = get_object_or_404(Category, id=pk)
        article = category.article.all()

        return  render(request, 'article_app/all_article.html', {'object_list': article})


class SearchView(ListView):
    model = Article
    template_name = 'article_app/all_article.html'
    context_object_name = 'object_list'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        return self.model.objects.filter(title__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        paginator = Paginator(context['object_list'], self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj

        return context


def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
        # print('unlike')
        return JsonResponse({"response": "unliked"})

    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
        # print('unlike')
        return JsonResponse({"response": "liked"})




















