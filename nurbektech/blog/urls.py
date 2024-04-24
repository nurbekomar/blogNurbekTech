from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("blog/", views.blog, name="blog"),
    path("project/", views.project, name="project"),
    path("post/<slug:post_slug>/", views.show_post, name="post"),
    path("category/<int:cat_id>/", views.show_category, name="category"),
]
