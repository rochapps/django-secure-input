from django.conf.urls import patterns, url
from django.views.generic import ListView, CreateView, DetailView

from .models import Comment
from .forms import SecureCommentForm, SecureWYSIWYGCommentForm

urlpatterns = patterns('',
    url(r'^create/$', CreateView.as_view(
            model = Comment,
            form_class=SecureCommentForm,
        ), name='comments_comment_create'),
    url(r'^create/editor/$', CreateView.as_view(
            model = Comment,
            form_class=SecureWYSIWYGCommentForm,
        ), name='comments_comment_wysiwyg'),
    url(r'^detail/(?P<pk>[\d]+)/$', DetailView.as_view(
            model = Comment,
        ), name='comments_comment_detail'),
    url(r'^$', ListView.as_view(
            model = Comment,
            template_name='index.html'
        ), name='comments_comment_list'),
)