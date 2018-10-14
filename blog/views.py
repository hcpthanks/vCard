from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Post, Comment


def blog_list(request):
    """
    博客列表页
    """

    object_list = Post.published.all()     #获得所有对象发布状态列表
    paginator = Paginator(object_list, 4)  # 创建分页对象paginator
    page = request.GET.get('page')         # 获得分页页码(地址栏page 参数)
    try:
        posts = paginator.page(page)  # 通过page方法获取页码数据
    except PageNotAnInteger:          # 如果页码不是一个整数
        posts = paginator.page(1)     # 则获取第一页数据
    except EmptyPage:                 # 如果页码为空
        posts = paginator.page(paginator.num_pages)  # 则获得最后一页数据
    return render(request, 'blog-list.html', {'page':page, 'posts':posts, 'paginator':paginator}) #呈现模板页面 blog-list,获得分页范围
     

    


def blog_detail(request, year, month, day, slug):
    """
    博客日志详情页
    """
    post = get_object_or_404(Post, 
    slug=slug,publish__year=year, publish__month=month, publish__day=day, status='published')
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
   
    return render(request, 'blog-detail.html', {'post':post, 'similar_posts':similar_posts})

