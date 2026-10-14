from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Register
    path("register/", views.RegisterView.as_view(), name="register"),

    # Login
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html"
        ),
        name="login",
    ),

    # Logout
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # About
    path("about/", views.about, name="about"),

    # Contact
    path("contact/", views.contact, name="contact"),

    # Blog post list
    path(
        "posts/",
        views.PostListView.as_view(),
        name="post_list",
    ),

    # My Posts
    path(
        "my-posts/",
        views.MyPostsView.as_view(),
        name="my_posts",
    ),

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