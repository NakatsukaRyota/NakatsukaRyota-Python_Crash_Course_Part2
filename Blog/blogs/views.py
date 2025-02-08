from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import BlogForm, EntryForm
from .models import Blog, Entry


def index(request):
    return render(request, "blogs/index.html")


def blogs(request):
    blogs = Blog.objects.order_by("data_added")
    context = {"blogs": blogs}
    return render(request, "blogs/blogs.html", context)


def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    entries = blog.entry_set.order_by("-date_added")
    context = {"blog": blog, "entries": entries}
    return render(request, "blogs/blog.html", context)


def new_blog(request):
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blogs")

    context = {"form": form}
    return render(request, "blogs/new_blog.html", context)


@login_required
def new_entry(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request.user)
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            new_entry.save()
            return redirect("blogs:blog", blog_id=blog_id)

    context = {"blog": blog, "form": form}
    return render(request, "blogs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    blog = entry.blog
    check_blog_owner(blog, request.user)
    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blog", blog_id=blog.id)

    context = {"entry": entry, "blog": blog, "form": form}
    return render(request, "blogs/edit_entry.html", context)


def check_blog_owner(blog, user):
    if blog.owner != user:
        raise Http404
