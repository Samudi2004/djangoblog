from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

# Creat your views here.


def home(request):
    return render(
        request,
        'blog/home.html',
        {'title': 'This is the Djangoblog Homepage.'},
    )


def about(request):
    return render(
        request, 'blog/about.html', {'content': 'This is the Djangoblog team.'}
    )


def contact(request):
    return render(
        request,
        'blog/contact.html',
        {'content1': 'This is the Djangoblog contact page.'},
    )

def post_list(request):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/post_list.html", {"page_obj": page_obj})