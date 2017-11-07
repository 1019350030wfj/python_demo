from django.utils.text import slugify
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
from comments.forms import CommentForm
from .models import Post,Category
# Create your views here.
import markdown
from markdown.extensions.toc import TocExtension

def index(request):
    # return HttpResponse("欢迎访问我的博客首页")
    # return render(request, 'blog/index.html', context={
    #                     'title': '博客首页',
    #                     'welcome': '欢迎来到我的博客首页',
    #                 })
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc'
    #                               ])


    # md = markdown.Markdown(extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc',
    # ])


    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'toc': md.toc,
               'form': form,
               'comment_list': comment_list}
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    # 记得在开始部分导入Category类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'blog/index.html', {'error_mg': error_msg})

    post_list = Post.objects.filter(title__contains=q)
    return render(request, 'blog/index.html', {'error_msg': error_msg, 'post_list': post_list})