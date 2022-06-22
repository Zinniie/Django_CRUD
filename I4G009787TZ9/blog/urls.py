import imp
from unicodedata import name
from django.urls import path

from I4G009787TZ9.blog.apps import BlogConfig
from .views import PostListView,PostCreateView,PostDetailView,PostUpdateView,PostDeleteView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="all"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("read/<slug:slug>", PostDetailView.as_view(), name="post_detail"),
    path("update/<slug:slug>", PostUpdateView.as_view(), name="post_update"),
    path("delete/<slug:slug>", PostDeleteView.as_view(), name="post_delete"),
    
]

