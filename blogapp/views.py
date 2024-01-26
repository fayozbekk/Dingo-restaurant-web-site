from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 1


class SingleBlogView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'single-blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        index = list(posts).index(self.object)
        context['posts'] = posts
        try:
            context['previous'] = posts[index - 1]
        except:
            context['previous'] = posts[index]
        try:
            context['previous'] = posts[index + 1]
        except:
            context['previous'] = posts[index]

        return context
