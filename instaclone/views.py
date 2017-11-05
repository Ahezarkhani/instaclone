from django.shortcuts import render
from django.views.generic.base import View

from database.models import Post, Like
from django.http import HttpResponseRedirect


class HomePage(View):
    def get(self, request):
        context = {}
        # code to query the database goes here!
        posts = Post.objects.all()[::-1]
        # add data to context
        context["posts"] = posts
        return render(request, 'index.html', context)


class PostPage(View):
    def get(self, request, postID):
        context = {}
        post = Post.objects.get(id=postID)
        context["post"] = post
        return render(request, 'post.html', context)

class CreatePost(View):
    def post(self, request):
        name = request.POST.get("name")
        url = request.POST.get("imgURL")
        caption = request.POST.get("caption")
        post = Post(imgURL=url, caption=caption, postedBy=name)
        post.save()
        return HttpResponseRedirect("/")