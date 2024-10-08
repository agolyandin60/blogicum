from django.http import Http404
from django.shortcuts import render

from .posts import posts


# Create your views here.
def index(request):
    template = 'blog/index.html'
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, pk):
    try:
        context = {'post': posts[pk]}
    except IndexError:
        raise Http404('Такой записи не существует')
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    return render(request, template, {'category_slug': category_slug})
