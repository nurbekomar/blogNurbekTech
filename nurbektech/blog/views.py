from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from blog.models import *

menu = [
    {"title": "Блог", "url_name": "blog"},
    {"title": "Проекты", "url_name": "project"},
]


def index(request):
    data = {"title": "Главная страница", "menu": menu}
    return render(request, "blog/index.html", context=data)


def blog(request):
    posts = Blog.objects.all()
    cats = Category.objects.all()
    data = {"title": "Блог", "menu": menu, "posts": posts, "cats": cats}
    return render(request, "blog/blog.html", context=data)


def project(request):
    data = {"title": "Проекты", "menu": menu}
    return render(request, "blog/project.html", context=data)


def contact(request):
    data = {"title": "Контакты", "menu": menu}
    return render(request, "blog/contact.html", context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)
    cats = Category.objects.all()
    data = {"title": "Пост", "menu": menu, "post": post, "cats": cats}
    return render(request, "blog/show_post.html", context=data)


def show_category(request, cat_id):
    posts = Blog.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {"title": "Блог", "menu": menu, "posts": posts, "cats": cats}
    return render(request, "blog/blog.html", context=data)


def page_not_found(request, exception):
    return render(request, "blog/page_not_found.html")
