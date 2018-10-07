from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Post, Comment


def blog_list(request):
    """
    博客列表页
    """
    # 获取所有日志信息
    # posts = Post.objects.all()
    #获取特定日志信息
    # posts = Post.objects.filter(status='published')
    # 日志管理器获取定义日志信息
    posts = Post.published.all()

    # 返回视图模板
    return render(request, 'blog-list.html', {'posts':posts})
    

    


def blog_detail(request, year, month, day, slug):
    """
    博客日志详情页
    """
    post = get_object_or_404(Post, 
    slug=slug,publish__year=year, publish__month=month, publish__day=day, status='published')
    return render(request, 'blog-detail.html', {'post':post})


