from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import models

from .models import Post, Category
from .forms import PostForm, RegisterForm


# ==========================================
# Home page
# ==========================================

def home(request):
    return render(
        request,
        "blog/home.html",
        {
            "title": "This is the Djangoblog Homepage.",
        }
    )
# About page
# ==========================================

def about(request):
    return render(
        request,
        "blog/about.html",
        {
            "content": "This is the Djangoblog team.",
        }
    )


# ==========================================
# Contact page
# ==========================================

def contact(request):
    return render(
        request,
        "blog/contact.html",
        {
            "content": "This is the Djangoblog contact page.",
        }
    )


# ==========================================
# User Registration
# ==========================================

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


register = RegisterView.as_view()


# ==========================================
# Blog Post List
# ==========================================

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 6

    def get_queryset(self):
        qs = Post.objects.filter(
            status="published"
        ).order_by("-created_at")

        category_slug = self.request.GET.get("category")

        if category_slug:
            qs = qs.filter(
                category__name__iexact=category_slug
            )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


post_list = PostListView.as_view()


# ==========================================
# My Posts
# ==========================================

class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/my_posts.html"
    paginate_by = 6
    login_url = "login"

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
        ).order_by("-created_at")


my_posts = MyPostsView.as_view()


# ==========================================
# Blog Post Detail
# ==========================================

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        posts = Post.objects.filter(
            status="published"
        )

        if self.request.user.is_authenticated:
            posts = Post.objects.filter(
                models.Q(status="published") |
                models.Q(author=self.request.user)
            )

        return posts


post_detail = PostDetailView.as_view()


# ==========================================
# Create Post
# ==========================================

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
            self.request,
            "Post published successfully!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={"slug": self.object.slug},
        )


post_create = PostCreateView.as_view()


# ==========================================
# Update Post
# ==========================================

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    login_url = "login"

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={"slug": self.object.slug},
        )


post_update = PostUpdateView.as_view()


# ==========================================
# Delete Post
# ==========================================

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
    login_url = "login"

    def test_func(self):
        return self.get_object().author == self.request.user


post_delete = PostDeleteView.as_view()


# ==========================================
# Custom 403 Page
# ==========================================

def custom_403(request, exception=None):
    return render(
        request,
        "blog/403.html",
        status=403,
    )