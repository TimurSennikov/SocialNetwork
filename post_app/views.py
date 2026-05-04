from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MyPostsView(TemplateView):
    template_name = 'post_app/my_posts.html'