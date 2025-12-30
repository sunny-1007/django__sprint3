from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


def index(request):
    """Render the main page with a list of published posts."""
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    ).order_by("-pub_date")
    template = "blog/index.html"
    context = {"post_list": post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Render the details page for a single post."""
    post = get_object_or_404(
        Post,
        pk=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    template = "blog/detail.html"
    context = {"post": post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Render a page with posts filtered by category."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
    ).order_by("-pub_date")
    template = "blog/category.html"
    context = {
        "category": category,
        "post_list": post_list,
    }
    return render(request, template, context)
