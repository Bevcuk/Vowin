from django.utils import timezone

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView
from django.views.generic import TemplateView

from blog.models import Post


class PostList(TemplateView):
    context_object_name = 'post'
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['post'] = Post.objects.all()
        return context


class DetailsList(TemplateView):
    context_object_name = 'post'
    template_name = 'blog/blog-items.html'

    def get_context_data(self, post_id, **kwargs):
        context = super(DetailsList, self).get_context_data()
        context['article'] = Post.objects.get(id=post_id)
        context['post'] = Post.objects.all()[:4]
        return context