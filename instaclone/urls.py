from django.conf.urls import url
from django.contrib import admin

from instaclone.views import HomePage, PostPage, CreatePost

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view()),
    url(r'^post/(?P<postID>[a-zA-Z0-9_.-]+)', PostPage.as_view()),
    url(r'^createPost', CreatePost.as_view())
]