from django.shortcuts import render
from django.http import HttpResponse

from config.models import SideBar
from .models import Post, Tag, Category
from django.views.generic import DetailView


# Create your views here.

class PostDetailView(DetailView):
    """用于展示详情的视图"""
    model = Post
    template_name = 'blog/detail.html'


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()
    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    print(context)
    return render(request, 'blog/list.html', context=context)
