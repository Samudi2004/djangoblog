"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

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
        auth_views.LogoutView.as_view(
            next_page="home"
        ),
        name="logout",
    ),

    # -----------------------------
    # Password Reset
    # -----------------------------
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="blog/password_reset.html"
        ),
        name="password_reset",
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="blog/password_reset_done.html"
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="blog/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="blog/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

    # Blog URLs
    path("", include("blog.urls")),
]

# Custom 403 handler
handler403 = "blog.views.custom_403"

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )