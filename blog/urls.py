from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Register
    path("register/", views.RegisterView.as_view(), name="register"),

    # About
    path("about/", views.about, name="about"),

    # Contact
    path("contact/", views.contact, name="contact"),

    # Blog post list
    path("posts/", views.PostListView.as_view(), name="post_list"),

    # Create post
    path(
        "posts/new/",
        views.PostCreateView.as_view(),
        name="post_create",
    ),

    # Edit post
    path(
        "posts/<slug:slug>/edit/",
        views.PostUpdateView.as_view(),
        name="post_edit",
    ),

    # Delete post
    path(
        "posts/<slug:slug>/delete/",
        views.PostDeleteView.as_view(),
        name="post_delete",
    ),

    # Post detail
    path(
        "posts/<slug:slug>/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
]