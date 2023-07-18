from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('post/<slug:slug>/', views.ArticleView.as_view(), name='post_view'),
    path('all_article', views.AllPostView.as_view(), name='all_post'),
    path('category/<int:pk>', views.AllCategoryView.as_view(), name='category_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),


]