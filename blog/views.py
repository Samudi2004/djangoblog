from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Category


# Home page
def home(request):
    return render(
        request,
        "blog/home.html",
        {
            "title": "This is the Djangoblog Homepage.",
        }
    )


# About page
def about(request):
    return render(
        request,
        "blog/about.html",
        {
            "content": "This is the Djangoblog team.",
        }
    )


# Contact page
def contact(request):
    return render(
        request,
        "blog/contact.html",
        {
            "content": "This is the Djangoblog contact page.",
        }
    )


# Blog post list page
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


post_list = PostListView.as_view()


# Blog post detail page
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self):
        return get_object_or_404(
            Post,
            slug=self.kwargs["slug"],
            status="published"
        )


post_detail = PostDetailView.as_view()


# Create post
class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "category", "tags", "status"]
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={"slug": self.object.slug}
        )


post_create = PostCreateView.as_view()


# Update post
class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "category", "tags", "status"]
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={"slug": self.object.slug}
        )


post_update = PostUpdateView.as_view()


# Delete post
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")


post_delete = PostDeleteView.as_view()