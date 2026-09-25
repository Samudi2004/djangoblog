from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post


# Home page
def home(request):
    return render(
        request,
        'blog/home.html',
        {'title': 'This is the Djangoblog Homepage.'},
    )


# About page
def about(request):
    return render(
        request,
        'blog/about.html',
        {'content': 'This is the Djangoblog team.'},
    )


# Contact page
def contact(request):
    return render(
        request,
        'blog/contact.html',
        {'content': 'This is the Djangoblog contact page.'},
    )


# Blog post list page
def post_list(request):
    posts = Post.objects.filter(
        status="published"
    ).order_by("-created_at")

    paginator = Paginator(posts, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/post_list.html",
        {"page_obj": page_obj}
    )


# Blog post detail page
def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status="published"
    )

    return render(
        request,
        "blog/post_detail.html",
        {"post": post}
    )